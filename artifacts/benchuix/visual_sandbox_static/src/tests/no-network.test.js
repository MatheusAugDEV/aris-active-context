export const no_remote_call_patterns = Object.freeze([
  "fe" + "tch(",
  "XML" + "Http" + "Request",
  "Web" + "Socket",
  "http" + "://",
  "https" + "://"
]);

export const no_remote_call_contract = {
  sourcePackOnly: true,
  staticReviewOnly: true,
  expectedMatchesInOperationalSource: 0
};

