#!/usr/bin/python3
"""how to read file"""


def read_file(filename="my_file_0"):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
