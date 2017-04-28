#!/usr/bin/node
const args = process.argv.slice(2);
const argsLen = args.length;
const num = parseInt(args[0]);
if (argsLen > 0 && !isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurances');
}
