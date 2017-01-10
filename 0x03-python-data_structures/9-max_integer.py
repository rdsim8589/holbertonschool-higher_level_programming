#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        return sorted(my_list, key=int, reverse=True)[0]
