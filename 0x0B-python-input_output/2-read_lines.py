#!/usr/bin/python3
"""
This module contains the function

read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Open and print nb_lines to std out
    Read entire file if nb_lines <= 0 or nb_lines >= total lines
    """
    line = 1
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0 or nb_lines >= myFile.read().count('\n'):
            print(myFile.read(), end="")
        else:
            myFile.seek(0)
            while line <= nb_lines:
                print(myFile.readline(), end="")
                line += 1
