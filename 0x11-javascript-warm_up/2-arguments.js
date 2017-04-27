#!/usr/bin/node
const numberArgs = process.argv.length - 3;
if (numberArgs < 0) {
  console.log('No argument');
} else if (numberArgs === 0) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
