#!/usr/bin/python3
def _uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end ="")
    print("")

def uppercase(str):
    print("".join(["{}".format(chr(ord(c) - 32))
                   if 97 <= ord(c) <= 122 else c
                   for c in str]))
