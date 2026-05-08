#!/usr/bin/python3
"""writes and object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """this function will save the obj to json file"""
    with open(filename, "w", encoding="utf=8") as f:
        json.dump(my_obj, f)
