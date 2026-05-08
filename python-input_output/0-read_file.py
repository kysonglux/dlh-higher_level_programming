#!/usr/bin/python3
"""how to read files"""


def read_file(filename="my_file_0"):
    """using parameter, read a file and print out """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
