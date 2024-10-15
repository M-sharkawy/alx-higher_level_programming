#!/usr/bin/python3

"""script that adds all arguments to a Python list"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

arg_0 = sys.argv[0]
arguments = sys.argv[1:]

try:
    existing_file = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_file = []

for arg in arguments:
    existing_file.append(arg)

save_to_json_file(existing_file, "add_item.json")
