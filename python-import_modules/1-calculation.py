#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    x = add(a , b)
    y = sub(a , b)
    z = mul(a , b)
    i = div(a , b)

    print("{} + {} = {}".format(a, b, x))
    print("{} - {} = {}".format(a, b, y))
    print("{} * {} = {}".format(a, b, z))
    print("{} / {} = {}".format(a, b, i))
