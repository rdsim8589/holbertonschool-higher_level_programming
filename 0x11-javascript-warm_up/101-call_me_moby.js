#!/usr/bin/node
function callMeMoby (num, func) {
  while (num > 0) {
    func();
    num--;
  }
}
module.exports.callMeMoby = callMeMoby;
