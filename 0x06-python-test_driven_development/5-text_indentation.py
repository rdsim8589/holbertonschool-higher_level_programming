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
    char_indent = ".?:"
    i = 0
    sentence = []
    while i < len(text):
        if text[i] == ' ' and text[i-1] in char_indent:
            i += 1
            pass
        sentence.append(text[i])
        if text[i] in char_indent:
            sentence.append("\n\n")
        i += 1
    print("".join(sentence), end ="")
