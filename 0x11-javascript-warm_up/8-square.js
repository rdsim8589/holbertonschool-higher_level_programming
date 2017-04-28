#!/usr/bin/node
const num = parseInt(process.argv.slice(2)[0]);
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('x'.repeat(num));
  }
} else {
  console.log('Missing size');
}
