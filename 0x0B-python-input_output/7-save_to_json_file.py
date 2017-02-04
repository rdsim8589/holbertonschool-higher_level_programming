#!/usr/bin/python3
"""
This module contains the function

save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using Json representation
    """
    import os
    import json
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
