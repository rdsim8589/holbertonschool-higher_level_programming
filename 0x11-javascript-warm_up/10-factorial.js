#!/usr/bin/node
function factorial (num) {
  let total = 1;
  if (isNaN(num)) {
    num = 1;
  }
  for (let i = 1; i <= num; i++) {
    total *= i;
  }
  console.log(total);
}

factorial(parseInt(process.argv.slice(2)[0]));
