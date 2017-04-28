#!/usr/bin/node
function addMeMaybe(num, func) {
  func(num + 1)
}
module.exports.addMeMaybe = addMeMaybe;
