#!/usr/bin/python3

import sys

if __name__ == "__main__":
    x = len(sys.argv)
    result = 0
    for i in range(1, x):
        result = int(sys.argv[i]) + result
    print("{}".format(result))
