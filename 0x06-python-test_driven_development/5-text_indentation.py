#!/usr/bin/python3
"""
This is the "Text Indextation" module

The "Text Indentation" module supplies the simple function/
to add two new line after a '.', '?', ':'.
"""


def text_indentation(text):
    """
    Prints a new string to add two new line after a '.', '?', ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    let_str = "".join([let + "\n\n" if let in "?.:" else let for let in text])
    print("\n".join([line.strip() for line in let_str.split("\n")]), end="")
