#!/usr/bin/node
const numberArgs = process.argv.length - 3;
if (numberArgs < 0) {
  console.log('No Arguement');
} else if (numberArgs === 0) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
