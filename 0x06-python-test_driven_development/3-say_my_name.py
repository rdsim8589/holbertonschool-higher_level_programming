#!/usr/bin/python3
"""
This is the "My Name Is" module

The My Name Is module supplies a simple function/
to print out the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    return: My name is first_name last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
