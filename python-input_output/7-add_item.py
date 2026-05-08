#!/usr/bin/python3
""" load, add all arguments to a list, save"""

import sys
import json
from os import path


def load_from_json_file(filename):
    """load file from json"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_to_json_file(my_obj, filename):
    """save object to json file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


filename = "add_item.json"

if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
