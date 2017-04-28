#!/usr/bin/node
const args = process.argv.slice(2);
const number = parseInt(args[0]);
if (args.length === 0 || isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
