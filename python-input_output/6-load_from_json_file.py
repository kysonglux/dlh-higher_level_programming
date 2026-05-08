#!/usr/bin/python3
"""Create object from a json file"""


import json


def load_from_json_file(filename):
    """ this function will creates an object from a json file """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
