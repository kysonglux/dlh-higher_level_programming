#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        "*": calculator_1.mul,
        "/": calculator_1.div,
    }
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    result = operator[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
