#!/usr/bin/python3
"""
This is the "Addition" module.

The Addition module supplies the simple function\
to add two int or floats together
"""


def add_integer(a, b):
   """
   Return the addition of a and b
   """
   if type(a) != int and type(a) != float:
      raise TypeError("a must be an integer")
   if type(b) != int and type(b) != float:
      raise TypeError("b must be an integer")
   return int(a) + int(b)
