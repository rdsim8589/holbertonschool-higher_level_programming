#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cp_list = my_list[:]
    for i in range(len(cp_list)):
        if cp_list[i] % 2 == 0:
            cp_list[i] = True
        else:
            cp_list[i] = False
    return cp_list
