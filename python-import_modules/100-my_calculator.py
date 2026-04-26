#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        x = add(a, b)
        print("{} + {} = {}".format(a, b, x))
    elif sys.argv[2] == "-":
        y = sub(a, b)
        print("{} - {} = {}".format(a, b, y))
    elif sys.argv[2] == "*":
        z = mul(a, b)
        print("{} * {} = {}".format(a, b, z))
    elif sys.argv[2] == "/":
        i = div(a, b)
        print("{} / {} = {}".format(a, b, i))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
