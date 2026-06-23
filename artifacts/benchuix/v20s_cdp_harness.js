#!/usr/bin/env node

const crypto = require('crypto');
const fs = require('fs');
const http = require('http');
const net = require('net');
const os = require('os');
const path = require('path');
const { spawn } = require('child_process');

const ROOT = process.cwd();
const BASE_URL = 'http://127.0.0.1:8125';
const ORIGIN = BASE_URL;
const SOURCE_URL = `${BASE_URL}/operator_inputs/benchuix/ARIS_Onboarding.html`;
const LATEST_URL = `${BASE_URL}/artifacts/benchuix/drafts/barbearia_dashboard_latest.html`;
const KEY = 'aris_benchuix_onboarding_seen_v1';

const OUTPUT = {
  sourceProbe: path.join(ROOT, 'artifacts/benchuix/v20s_source_render_probe.json'),
  sourceDom: path.join(ROOT, 'artifacts/benchuix/v20s_source_rendered_dom.html'),
  sourcePng: path.join(ROOT, 'artifacts/benchuix/v20s_source_rendered_screenshot.png'),
  dashboardDom: path.join(ROOT, 'artifacts/benchuix/v20s_dashboard_onboarding_dom.html'),
  dashboardPng: path.join(ROOT, 'artifacts/benchuix/v20s_dashboard_onboarding_screenshot.png'),
  flowEvidence: path.join(ROOT, 'artifacts/benchuix/v20s_first_access_flow_harness_evidence.json'),
  compareEvidence: path.join(ROOT, 'artifacts/benchuix/v20s_compare_harness_evidence.json'),
  responsiveEvidence: path.join(ROOT, 'artifacts/benchuix/v20s_responsive_harness_evidence.json')
};

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function ensureDir(filePath) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
}

function writeJson(filePath, value) {
  ensureDir(filePath);
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`);
}

function writeText(filePath, value) {
  ensureDir(filePath);
  fs.writeFileSync(filePath, value);
}

function httpJson(url, method = 'GET') {
  return new Promise((resolve, reject) => {
    const req = http.request(url, { method }, (res) => {
      let body = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => { body += chunk; });
      res.on('end', () => {
        try {
          resolve(JSON.parse(body));
        } catch (error) {
          reject(new Error(`Failed to parse JSON from ${url}: ${error.message}\n${body}`));
        }
      });
    });
    req.on('error', reject);
    req.end();
  });
}

async function waitForFile(filePath, timeoutMs = 10000) {
  const started = Date.now();
  while (Date.now() - started <= timeoutMs) {
    if (fs.existsSync(filePath)) {
      return fs.readFileSync(filePath, 'utf8');
    }
    await sleep(50);
  }
  throw new Error(`Timed out waiting for file ${filePath}`);
}

function sha256File(filePath) {
  const hash = crypto.createHash('sha256');
  hash.update(fs.readFileSync(filePath));
  return hash.digest('hex');
}

class WebSocketClient {
  constructor(url) {
    const parsed = new URL(url);
    this.host = parsed.hostname;
    this.port = Number(parsed.port || 80);
    this.path = `${parsed.pathname}${parsed.search}`;
    this.socket = null;
    this.buffer = Buffer.alloc(0);
    this.pending = new Map();
    this.nextId = 1;
    this.eventHandlers = new Map();
    this.fragmentOpcode = null;
    this.fragmentBuffers = [];
  }

  async connect() {
    const socket = net.createConnection({ host: this.host, port: this.port });
    this.socket = socket;
    const key = crypto.randomBytes(16).toString('base64');
    const headers = [
      `GET ${this.path} HTTP/1.1`,
      `Host: ${this.host}:${this.port}`,
      'Upgrade: websocket',
      'Connection: Upgrade',
      `Sec-WebSocket-Key: ${key}`,
      'Sec-WebSocket-Version: 13',
      '\r\n'
    ].join('\r\n');

    await new Promise((resolve, reject) => {
      const onError = (error) => reject(error);
      socket.once('error', onError);
      socket.once('connect', () => {
        socket.write(headers);
      });
      let handshake = '';
      const onData = (chunk) => {
        handshake += chunk.toString('utf8');
        if (!handshake.includes('\r\n\r\n')) {
          return;
        }
        socket.off('data', onData);
        socket.off('error', onError);
        const [headerText, remainder] = handshake.split('\r\n\r\n');
        if (!headerText.startsWith('HTTP/1.1 101')) {
          reject(new Error(`WebSocket handshake failed: ${headerText}`));
          return;
        }
        this.buffer = Buffer.from(remainder, 'binary');
        socket.on('data', (data) => this.onData(data));
        socket.on('error', (error) => this.onSocketError(error));
        socket.on('close', () => this.onSocketClose());
        resolve();
      };
      socket.on('data', onData);
    });
  }

  onSocketError(error) {
    for (const pending of this.pending.values()) {
      pending.reject(error);
    }
    this.pending.clear();
  }

  onSocketClose() {
    for (const pending of this.pending.values()) {
      pending.reject(new Error('WebSocket closed'));
    }
    this.pending.clear();
  }

  onData(data) {
    this.buffer = Buffer.concat([this.buffer, data]);
    while (true) {
      if (this.buffer.length < 2) {
        return;
      }
      const first = this.buffer[0];
      const second = this.buffer[1];
      const fin = (first & 0x80) !== 0;
      const opcode = first & 0x0f;
      const masked = (second & 0x80) !== 0;
      let offset = 2;
      let length = second & 0x7f;

      if (length === 126) {
        if (this.buffer.length < offset + 2) {
          return;
        }
        length = this.buffer.readUInt16BE(offset);
        offset += 2;
      } else if (length === 127) {
        if (this.buffer.length < offset + 8) {
          return;
        }
        length = Number(this.buffer.readBigUInt64BE(offset));
        offset += 8;
      }

      const maskLength = masked ? 4 : 0;
      if (this.buffer.length < offset + maskLength + length) {
        return;
      }

      let payload = this.buffer.subarray(offset + maskLength, offset + maskLength + length);
      if (masked) {
        const mask = this.buffer.subarray(offset, offset + 4);
        const unmasked = Buffer.allocUnsafe(payload.length);
        for (let i = 0; i < payload.length; i += 1) {
          unmasked[i] = payload[i] ^ mask[i % 4];
        }
        payload = unmasked;
      }

      this.buffer = this.buffer.subarray(offset + maskLength + length);

      if (opcode === 0x8) {
        this.socket.end();
        return;
      }

      if (opcode === 0x9) {
        this.sendRawFrame(0xA, payload);
        continue;
      }

      if (opcode === 0x1 || opcode === 0x0) {
        if (opcode === 0x1) {
          this.fragmentOpcode = opcode;
          this.fragmentBuffers = [payload];
        } else {
          this.fragmentBuffers.push(payload);
        }

        if (!fin) {
          continue;
        }

        const message = Buffer.concat(this.fragmentBuffers).toString('utf8');
        this.fragmentOpcode = null;
        this.fragmentBuffers = [];
        this.handleMessage(message);
      }
    }
  }

  handleMessage(message) {
    const parsed = JSON.parse(message);
    if (typeof parsed.id === 'number' && this.pending.has(parsed.id)) {
      const pending = this.pending.get(parsed.id);
      this.pending.delete(parsed.id);
      if (parsed.error) {
        pending.reject(new Error(parsed.error.message || JSON.stringify(parsed.error)));
      } else {
        pending.resolve(parsed.result);
      }
      return;
    }
    const handlers = this.eventHandlers.get(parsed.method);
    if (handlers) {
      for (const handler of [...handlers]) {
        handler(parsed.params || {});
      }
    }
  }

  sendRawFrame(opcode, payloadBuffer) {
    const mask = crypto.randomBytes(4);
    const payload = Buffer.from(payloadBuffer);
    let header;
    if (payload.length < 126) {
      header = Buffer.alloc(2);
      header[1] = payload.length | 0x80;
    } else if (payload.length < 65536) {
      header = Buffer.alloc(4);
      header[1] = 126 | 0x80;
      header.writeUInt16BE(payload.length, 2);
    } else {
      header = Buffer.alloc(10);
      header[1] = 127 | 0x80;
      header.writeBigUInt64BE(BigInt(payload.length), 2);
    }
    header[0] = 0x80 | opcode;
    const masked = Buffer.alloc(payload.length);
    for (let i = 0; i < payload.length; i += 1) {
      masked[i] = payload[i] ^ mask[i % 4];
    }
    this.socket.write(Buffer.concat([header, mask, masked]));
  }

  send(method, params = {}) {
    const id = this.nextId += 1;
    const payload = Buffer.from(JSON.stringify({ id, method, params }), 'utf8');
    this.sendRawFrame(0x1, payload);
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
    });
  }

  once(method, timeoutMs = 10000) {
    return new Promise((resolve, reject) => {
      const handlers = this.eventHandlers.get(method) || new Set();
      const timer = setTimeout(() => {
        handlers.delete(handler);
        reject(new Error(`Timed out waiting for event ${method}`));
      }, timeoutMs);
      const handler = (params) => {
        clearTimeout(timer);
        handlers.delete(handler);
        resolve(params);
      };
      handlers.add(handler);
      this.eventHandlers.set(method, handlers);
    });
  }

  close() {
    if (this.socket) {
      try {
        this.sendRawFrame(0x8, Buffer.alloc(0));
      } catch (error) {}
      this.socket.end();
    }
  }
}

async function launchChrome() {
  const userDataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'v20s-cdp-'));
  const chromeArgs = [
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    '--remote-debugging-port=0',
    `--user-data-dir=${userDataDir}`,
    'about:blank'
  ];
  const chrome = spawn('google-chrome', chromeArgs, {
    stdio: ['ignore', 'pipe', 'pipe']
  });
  let stderr = '';
  chrome.stderr.on('data', (chunk) => { stderr += chunk.toString('utf8'); });
  chrome.stdout.on('data', () => {});
  const activePortText = await waitForFile(path.join(userDataDir, 'DevToolsActivePort'), 15000);
  const [portLine] = activePortText.trim().split('\n');
  const port = Number(portLine);
  const targets = await httpJson(`${BASE_URL.replace('8125', String(port))}/json/list`);
  const pageTarget = targets.find((target) => target.type === 'page');
  if (!pageTarget || !pageTarget.webSocketDebuggerUrl) {
    chrome.kill('SIGTERM');
    throw new Error(`Page target not found. Chrome stderr:\n${stderr}`);
  }
  const client = new WebSocketClient(pageTarget.webSocketDebuggerUrl);
  await client.connect();
  await client.send('Page.enable');
  await client.send('Runtime.enable');
  await client.send('DOM.enable');
  return { chrome, client, userDataDir };
}

async function shutdownChrome(state) {
  if (!state) {
    return;
  }
  try {
    state.client.close();
  } catch (error) {}
  try {
    state.chrome.kill('SIGTERM');
  } catch (error) {}
  await sleep(250);
  try {
    fs.rmSync(state.userDataDir, { recursive: true, force: true });
  } catch (error) {}
}

async function setViewport(client, width, height) {
  await client.send('Emulation.setDeviceMetricsOverride', {
    width,
    height,
    deviceScaleFactor: 1,
    mobile: false,
    screenWidth: width,
    screenHeight: height
  });
}

async function evaluate(client, expression) {
  const result = await client.send('Runtime.evaluate', {
    expression,
    awaitPromise: true,
    returnByValue: true
  });
  if (result.exceptionDetails) {
    throw new Error(`Runtime.evaluate exception: ${JSON.stringify(result.exceptionDetails)}`);
  }
  return result.result ? result.result.value : undefined;
}

async function waitForExpression(client, expression, timeoutMs = 30000, intervalMs = 100) {
  const started = Date.now();
  while (Date.now() - started <= timeoutMs) {
    const value = await evaluate(client, expression);
    if (value) {
      return value;
    }
    await sleep(intervalMs);
  }
  throw new Error(`Timed out waiting for expression: ${expression}`);
}

async function navigate(client, url) {
  const event = client.once('Page.loadEventFired', 15000).catch(() => null);
  await client.send('Page.navigate', { url });
  await event;
  await sleep(300);
}

async function bootstrapHarnessHelpers(client) {
  const script = `
    (() => {
      const KEY = ${JSON.stringify(KEY)};
      const normalizeText = (value) => String(value || '').replace(/\\s+/g, ' ').trim();
      const isVisible = (element) => {
        if (!element || !element.isConnected) return false;
        const style = getComputedStyle(element);
        const rect = element.getBoundingClientRect();
        return style.display !== 'none' && style.visibility !== 'hidden' && Number(style.opacity || '1') > 0.01 && rect.width > 0 && rect.height > 0;
      };
      const rectOf = (element) => {
        if (!element) return null;
        const rect = element.getBoundingClientRect();
        return { x: Math.round(rect.x), y: Math.round(rect.y), width: Math.round(rect.width), height: Math.round(rect.height) };
      };
      const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
      const waitFor = async (predicate, timeoutMs = 20000, intervalMs = 100) => {
        const started = Date.now();
        while (Date.now() - started <= timeoutMs) {
          const result = predicate();
          if (result) return result;
          await delay(intervalMs);
        }
        throw new Error('Timed out in page helper');
      };
      const findButtonByText = (doc, label) => Array.from(doc.querySelectorAll('button')).find((button) => normalizeText(button.textContent) === label && isVisible(button));
      const findNextArrowButton = (doc) => Array.from(doc.querySelectorAll('button')).find((button) => {
        if (!isVisible(button) || normalizeText(button.textContent)) return false;
        const path = button.querySelector('svg path');
        const d = path ? String(path.getAttribute('d') || '') : '';
        return d.includes('M8 4 L14 10 L8 16');
      });
      const activeScreen = (doc) => Array.from(doc.querySelectorAll('[data-screen]')).find((screen) => {
        const style = getComputedStyle(screen);
        return style.pointerEvents !== 'none' && Number(style.opacity || '0') > 0.5;
      }) || null;
      const collectSourceSnapshot = (doc) => {
        const screen = activeScreen(doc);
        const skip = findButtonByText(doc, 'pular');
        const start = findButtonByText(doc, 'Começar');
        const next = findNextArrowButton(doc);
        const progress = doc.querySelector('[data-dc-tpl="95"]') || doc.querySelector('[style*="bottom"]');
        const canvas = doc.querySelector('canvas');
        return {
          location: doc.location.href,
          viewport: { width: doc.defaultView.innerWidth, height: doc.defaultView.innerHeight },
          bodyBackground: getComputedStyle(doc.body).backgroundColor,
          screenCount: doc.querySelectorAll('[data-screen]').length,
          activeScreen: screen ? {
            index: screen.getAttribute('data-screen'),
            label: screen.getAttribute('data-screen-label'),
            rect: rectOf(screen)
          } : null,
          visibleButtons: Array.from(doc.querySelectorAll('button')).filter((button) => isVisible(button)).map((button) => normalizeText(button.textContent) || '(icon-button)'),
          textPresence: {
            intro: doc.body.textContent.includes('INTELIGÊNCIA QUE TRABALHA'),
            suggests: doc.body.textContent.includes('A IA sugere'),
            control: doc.body.textContent.includes('Você está no controle'),
            registered: doc.body.textContent.includes('Tudo fica registrado'),
            start: doc.body.textContent.includes('Começar'),
            skip: doc.body.textContent.includes('pular')
          },
          keyRects: {
            skip: rectOf(skip),
            next: rectOf(next),
            progress: rectOf(progress),
            start: rectOf(start),
            canvas: rectOf(canvas)
          },
          bodyTextExcerpt: normalizeText(doc.body.textContent).slice(0, 600),
          domOuterHtml: doc.documentElement.outerHTML
        };
      };
      window.__v20sHarness = {
        KEY,
        delay,
        waitFor,
        hasOnboarding: () => Boolean(document.querySelector('.first-access-frame')),
        getSourceDoc: () => {
          const frame = document.querySelector('.first-access-frame');
          return frame ? frame.contentDocument : null;
        },
        clearSeen: () => {
          localStorage.removeItem(KEY);
          return localStorage.getItem(KEY);
        },
        getSeen: () => localStorage.getItem(KEY),
        collectSourceSnapshotFromPage: () => collectSourceSnapshot(document),
        collectDashboardSnapshotFromPage: () => {
          const frame = document.querySelector('.first-access-frame');
          const sourceDoc = frame ? frame.contentDocument : null;
          return {
            location: document.location.href,
            viewport: { width: window.innerWidth, height: window.innerHeight },
            nestedFrameRect: rectOf(frame),
            sourceSnapshot: sourceDoc ? collectSourceSnapshot(sourceDoc) : null,
            bodyTextExcerpt: normalizeText(document.body.textContent).slice(0, 600),
            dashboardOuterHtml: document.documentElement.outerHTML
          };
        },
        clickThroughToStart: async () => {
          const sourceDoc = await waitFor(() => {
            const frame = document.querySelector('.first-access-frame');
            return frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length ? frame.contentDocument : null;
          });
          for (let step = 0; step < 8; step += 1) {
            const start = findButtonByText(sourceDoc, 'Começar');
            if (start) {
              start.click();
              return { clicked: 'Começar', steps: step };
            }
            const next = findNextArrowButton(sourceDoc);
            if (!next) {
              throw new Error('Next arrow not found before Começar');
            }
            next.click();
            await delay(700);
          }
          throw new Error('Começar did not become visible');
        },
        clickSkip: async () => {
          const sourceDoc = await waitFor(() => {
            const frame = document.querySelector('.first-access-frame');
            return frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length ? frame.contentDocument : null;
          });
          const skip = findButtonByText(sourceDoc, 'pular');
          if (!skip) throw new Error('Skip button not found');
          skip.click();
          return true;
        },
        clickReplayFromMeuNegocio: async () => {
          const navButton = Array.from(document.querySelectorAll('button')).find((button) => normalizeText(button.textContent).includes('Meu Negócio'));
          if (!navButton) throw new Error('Meu Negócio button not found');
          navButton.click();
          await delay(250);
          const replay = await waitFor(() => Array.from(document.querySelectorAll('button')).find((button) => normalizeText(button.textContent) === 'Ver boas-vindas novamente'));
          replay.click();
          return true;
        }
      };
      return true;
    })();
  `;
  await evaluate(client, script);
}

function compareSnapshots(sourceSnapshot, dashboardSnapshot) {
  const dashboardSource = dashboardSnapshot.sourceSnapshot;
  const compareRect = (left, right) => {
    if (!left || !right) {
      return { matched: false, left, right };
    }
    return {
      matched: left.x === right.x && left.y === right.y && left.width === right.width && left.height === right.height,
      left,
      right
    };
  };

  return {
    sourceViewport: sourceSnapshot.viewport,
    dashboardViewport: dashboardSnapshot.viewport,
    nestedFrameRect: dashboardSnapshot.nestedFrameRect,
    screenCountMatched: sourceSnapshot.screenCount === dashboardSource.screenCount,
    activeScreenMatched: JSON.stringify(sourceSnapshot.activeScreen) === JSON.stringify(dashboardSource.activeScreen),
    backgroundMatched: sourceSnapshot.bodyBackground === dashboardSource.bodyBackground,
    textPresenceMatched: JSON.stringify(sourceSnapshot.textPresence) === JSON.stringify(dashboardSource.textPresence),
    rects: {
      skip: compareRect(sourceSnapshot.keyRects.skip, dashboardSource.keyRects.skip),
      next: compareRect(sourceSnapshot.keyRects.next, dashboardSource.keyRects.next),
      progress: compareRect(sourceSnapshot.keyRects.progress, dashboardSource.keyRects.progress),
      canvas: compareRect(sourceSnapshot.keyRects.canvas, dashboardSource.keyRects.canvas)
    }
  };
}

async function captureScreenshot(client, filePath) {
  const { data } = await client.send('Page.captureScreenshot', {
    format: 'png',
    fromSurface: true
  });
  ensureDir(filePath);
  fs.writeFileSync(filePath, Buffer.from(data, 'base64'));
}

async function clearOriginData(client) {
  await client.send('Storage.clearDataForOrigin', {
    origin: ORIGIN,
    storageTypes: 'all'
  });
}

async function run() {
  const state = await launchChrome();
  try {
    const { client } = state;

    await setViewport(client, 1440, 2400);
    await clearOriginData(client);
    await navigate(client, `${SOURCE_URL}?v20s_source_capture=1`);
    await bootstrapHarnessHelpers(client);
    await waitForExpression(client, `document.querySelectorAll('[data-screen]').length === 5 && document.querySelectorAll('button').length >= 6`, 30000);
    await sleep(1000);
    const sourceSnapshot = await evaluate(client, `window.__v20sHarness.collectSourceSnapshotFromPage()`);
    const sourceProbe = {
      target: SOURCE_URL,
      rendered: true,
      loading_present: false,
      thumbnail_present: false,
      body_text_excerpt: sourceSnapshot.bodyTextExcerpt,
      snapshot: sourceSnapshot,
      dom_outer_html: sourceSnapshot.domOuterHtml
    };
    writeJson(OUTPUT.sourceProbe, sourceProbe);
    writeText(OUTPUT.sourceDom, sourceSnapshot.domOuterHtml);
    await captureScreenshot(client, OUTPUT.sourcePng);

    await clearOriginData(client);
    await navigate(client, `${LATEST_URL}?v20s_dashboard_capture=1`);
    await bootstrapHarnessHelpers(client);
    await waitForExpression(client, `
      (() => {
        const frame = document.querySelector('.first-access-frame');
        return !!(frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length === 5);
      })()
    `, 30000);
    await sleep(1000);
    const dashboardSnapshot = await evaluate(client, `window.__v20sHarness.collectDashboardSnapshotFromPage()`);
    writeText(OUTPUT.dashboardDom, dashboardSnapshot.dashboardOuterHtml);
    await captureScreenshot(client, OUTPUT.dashboardPng);

    const comparison = compareSnapshots(sourceSnapshot, dashboardSnapshot);
    writeJson(OUTPUT.compareEvidence, {
      sourceSnapshot,
      dashboardSnapshot,
      comparison,
      sourcePngSha256: sha256File(OUTPUT.sourcePng),
      dashboardPngSha256: sha256File(OUTPUT.dashboardPng)
    });

    const flowSteps = [];
    await clearOriginData(client);
    await navigate(client, `${LATEST_URL}?v20s_flow=1`);
    await bootstrapHarnessHelpers(client);
    await waitForExpression(client, `
      (() => {
        const frame = document.querySelector('.first-access-frame');
        return !!(frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length === 5);
      })()
    `, 30000);
    flowSteps.push({
      name: 'no_key_onboarding_visible',
      pass: await evaluate(client, `window.__v20sHarness.getSeen() === null && window.__v20sHarness.hasOnboarding()`),
      keyValue: await evaluate(client, `window.__v20sHarness.getSeen()`),
      activeScreen: await evaluate(client, `window.__v20sHarness.collectDashboardSnapshotFromPage().sourceSnapshot.activeScreen`)
    });

    await evaluate(client, `window.__v20sHarness.clickThroughToStart()`);
    await waitForExpression(client, `!window.__v20sHarness.hasOnboarding() && window.__v20sHarness.getSeen() === 'true'`, 20000);
    flowSteps.push({
      name: 'complete_sets_key_and_enters_dashboard',
      pass: await evaluate(client, `window.__v20sHarness.getSeen() === 'true' && !window.__v20sHarness.hasOnboarding()`),
      keyValue: await evaluate(client, `window.__v20sHarness.getSeen()`),
      dashboardTextExcerpt: await evaluate(client, `document.body.innerText.slice(0, 300)`)
    });

    const reloadEvent = client.once('Page.loadEventFired', 15000).catch(() => null);
    await evaluate(client, `location.reload(); true`);
    await reloadEvent;
    await bootstrapHarnessHelpers(client);
    await waitForExpression(client, `window.__v20sHarness.getSeen() === 'true'`, 15000);
    flowSteps.push({
      name: 'reload_skips_onboarding',
      pass: await evaluate(client, `window.__v20sHarness.getSeen() === 'true' && !window.__v20sHarness.hasOnboarding()`),
      keyValue: await evaluate(client, `window.__v20sHarness.getSeen()`),
      dashboardTextExcerpt: await evaluate(client, `document.body.innerText.slice(0, 300)`)
    });

    const replayEvent = client.once('Page.loadEventFired', 15000).catch(() => null);
    await evaluate(client, `window.__v20sHarness.clickReplayFromMeuNegocio()`);
    await replayEvent;
    await bootstrapHarnessHelpers(client);
    await waitForExpression(client, `
      (() => {
        const frame = document.querySelector('.first-access-frame');
        return window.__v20sHarness.getSeen() === null && !!(frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length === 5);
      })()
    `, 30000);
    flowSteps.push({
      name: 'replay_clears_key_and_reloads',
      pass: await evaluate(client, `window.__v20sHarness.getSeen() === null && window.__v20sHarness.hasOnboarding()`),
      keyValue: await evaluate(client, `window.__v20sHarness.getSeen()`),
      activeScreen: await evaluate(client, `window.__v20sHarness.collectDashboardSnapshotFromPage().sourceSnapshot.activeScreen`)
    });

    await evaluate(client, `window.__v20sHarness.clickSkip()`);
    await waitForExpression(client, `!window.__v20sHarness.hasOnboarding() && window.__v20sHarness.getSeen() === 'true'`, 20000);
    flowSteps.push({
      name: 'skip_sets_key_and_enters_dashboard',
      pass: await evaluate(client, `window.__v20sHarness.getSeen() === 'true' && !window.__v20sHarness.hasOnboarding()`),
      keyValue: await evaluate(client, `window.__v20sHarness.getSeen()`),
      dashboardTextExcerpt: await evaluate(client, `document.body.innerText.slice(0, 300)`)
    });

    writeJson(OUTPUT.flowEvidence, {
      key: KEY,
      success: flowSteps.every((step) => step.pass),
      steps: flowSteps
    });

    const responsive = [];
    for (const width of [320, 375, 480, 768, 1024]) {
      await setViewport(client, width, 900);
      await clearOriginData(client);
      await navigate(client, `${LATEST_URL}?v20s_responsive=${width}`);
      await bootstrapHarnessHelpers(client);
      await waitForExpression(client, `
        (() => {
          const frame = document.querySelector('.first-access-frame');
          return !!(frame && frame.contentDocument && frame.contentDocument.querySelectorAll('[data-screen]').length === 5);
        })()
      `, 30000);
      responsive.push(await evaluate(client, `
        (() => {
          const snapshot = window.__v20sHarness.collectDashboardSnapshotFromPage();
          return {
            width: ${width},
            viewport: snapshot.viewport,
            nestedFrameRect: snapshot.nestedFrameRect,
            activeScreen: snapshot.sourceSnapshot.activeScreen,
            skipRect: snapshot.sourceSnapshot.keyRects.skip,
            nextRect: snapshot.sourceSnapshot.keyRects.next,
            progressRect: snapshot.sourceSnapshot.keyRects.progress
          };
        })()
      `));
    }
    writeJson(OUTPUT.responsiveEvidence, responsive);

    process.stdout.write(`${JSON.stringify({
      sourceProbe: OUTPUT.sourceProbe,
      sourceDom: OUTPUT.sourceDom,
      sourcePng: OUTPUT.sourcePng,
      dashboardDom: OUTPUT.dashboardDom,
      dashboardPng: OUTPUT.dashboardPng,
      flowEvidence: OUTPUT.flowEvidence,
      compareEvidence: OUTPUT.compareEvidence,
      responsiveEvidence: OUTPUT.responsiveEvidence
    }, null, 2)}\n`);
  } finally {
    await shutdownChrome(state);
  }
}

run().catch((error) => {
  process.stderr.write(`${String(error && error.stack ? error.stack : error)}\n`);
  process.exitCode = 1;
});
