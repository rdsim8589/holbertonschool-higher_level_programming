#!/bin/usr/python3
"""
This is the "Print Square" module

The Print Square module supplies the simple function\
to print a square of # of a size
"""


def print_square(size):
    """
    Return the square of # of size x size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("\n".join(["#" * size for i in range(size)]))
