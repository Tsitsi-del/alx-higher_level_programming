#!/usr/bin/python3
"""
7-add_item.py
"""
import sys
import json
import os.path


save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

file_name = "add_item.json"
json_list = []

if os.path.exists(file_name):
    json_list = load_from_json_file(file_name)

for index in range(1, len(sys.argv)):
    json_list.append(sys.argv[index])

save_to_json_file(json_list, file_name)
