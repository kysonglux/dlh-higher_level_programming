#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == "+":
        x = add(a, b)
        print("{} + {} = {}".format(a, b, x))
    elif op == "-":
        y = sub(a, b)
        print("{} - {} = {}".format(a, b, y))
    elif op == "*":
        z = mul(a, b)
        print("{} * {} = {}".format(a, b, z))
    elif op == "/":
        i = div(a, b)
        print("{} / {} = {}".format(a, b, i))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
