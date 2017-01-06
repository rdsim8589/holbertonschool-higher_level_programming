#!/usr/bin/python3
from calculator_1 import sub, add, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    signs = "+-x/"
    SignByFun = {"-": sub, "+": add, "x": mul, "/": div}
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op in signs:
        print("{:d} {} {:d} = {:d}".format(a, op, b, SignByFun[op](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
