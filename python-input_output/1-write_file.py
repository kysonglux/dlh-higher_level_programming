#!/usr/bin/python3
"""how to write a file"""


def write_file(filename="my_first_file", text=""):
    """creating or overwriting file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
