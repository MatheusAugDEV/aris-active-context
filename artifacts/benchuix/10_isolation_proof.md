# BENCHUIX-10 Isolation Proof

## definição da prova de isolamento

A prova de isolamento define as garantias minimas para que o preview de BENCHUIX-10 permaneça apenas simulacao candidata, sem qualquer efeito real.

## synthetic-only boundary

O boundary desta fase aceita apenas contexto sintetico, defaults controlados e artefatos documentais do active-context. Nenhuma entrada externa em tempo real e aceita.

## entradas permitidas

- automacao candidata vinda de BENCHUIX-09;
- playbooks sinteticos de BENCHUIX-08;
- contexto sintetico de negocio ja definido na trilha;
- limites e regras descritos no proprio protocolo de preview.

## saídas permitidas

- preview textual deterministico;
- diff antes/depois em linguagem humana;
- estimativa candidata de impacto, risco e custo;
- justificativa de bloqueio ou degraded quando necessario.

## garantias de não toque em dado real

- sem leitura de dado de cliente;
- sem agenda real;
- sem estoque real;
- sem historico real;
- sem dado financeiro real;
- sem credencial, token ou secret.

## garantias de não chamada a serviço real

- sem API externa;
- sem WhatsApp real;
- sem e-mail real;
- sem push real;
- sem PSP real;
- sem CRM real;
- sem calendario real.

## garantias de não mutação de estado

- sem escrita de estado persistente;
- sem confirmacao real;
- sem alteracao de fila real;
- sem criar ou atualizar automacao real;
- sem side effect fora do artifact-only.

## garantias de não runtime

- sem abrir executor;
- sem acionar job real;
- sem runtime visivel ao cliente;
- sem caminho de deploy, apply ou producao.

## matriz de bloqueios

- qualquer dependencia de dado real: BLOCK;
- qualquer chamada de servico real: BLOCK;
- qualquer mutacao de estado: BLOCK;
- qualquer runtime real ou visivel: BLOCK;
- qualquer acao sensivel sem preview legivel: BLOCK;
- qualquer falta de explicacao sobre isolamento: BLOCK.

## evidência esperada para fases futuras

- preview legivel preservado;
- diff antes/depois preservado;
- impacto, risco e custo descritos;
- motivo de bloqueio quando necessario;
- confirmacao explicita de que nada real foi tocado.

## limitações explícitas

- esta prova nao valida produto real;
- esta prova nao substitui Bedrock Gate;
- esta prova nao autoriza runtime;
- esta prova nao autoriza aprovar sem inbox dedicada;
- esta prova nao mede resultado real, apenas expectativa sintetica e isolada.
