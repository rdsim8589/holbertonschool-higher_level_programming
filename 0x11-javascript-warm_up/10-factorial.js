#!/usr/bin/node
let total = 1;
let num = parseInt(process.argv.slice(2)[0]);
if (isNaN(num)) {
  num = 1;
}
while (num > 0) {
  total *= num;
  num--;
}
console.log(total);
