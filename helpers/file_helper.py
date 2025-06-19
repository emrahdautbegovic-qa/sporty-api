import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)  # loads JSON data into a Python dict
    return data