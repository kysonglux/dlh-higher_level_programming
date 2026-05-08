#!/usr/bin/python3
""" how to use append """


def append_write(filename="", text=""):
    """ this function will append a string at the end of a text file"""
    with open(filename, "a", encoding="utf8") as f:
        return (f.write(text))
