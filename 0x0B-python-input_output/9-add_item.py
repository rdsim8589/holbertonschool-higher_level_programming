#!/usr/bin/python3
"""
This module contains


"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    try:
        list_obj = load_from_json_file(filename)
    except Exception as e:
        list_obj = []
    save_to_json_file(list_obj + argv[1:], filename)
