#!/usr/bin/env python3
"""converting csv data to json format"""


import csv
import json
import os


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file.
    Return true on success, False on failure."""
    if not os.path.exists(csv_filename):
        return Flase
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open("data.json", mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True

    except (FileNotFoundError, FileExistsError):
        return False
