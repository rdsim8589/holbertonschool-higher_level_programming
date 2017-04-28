#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}
