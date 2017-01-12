#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is not None:
        for key in my_dict.keys():
            if my_dict[key] == max(list(my_dict.values())):
                return key
