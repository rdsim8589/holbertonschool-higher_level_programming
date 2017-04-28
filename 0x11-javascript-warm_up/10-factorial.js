#!/usr/bin/node
function factorial (num) {
  let total = 1;
  if (isNaN(num)) {
    num = 1;
  }
  while (num > 0) {
    total *= num;
    num--;
  }
  console.log(total);
}

factorial(parseInt(process.argv.slice(2)[0]));
