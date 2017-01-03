#!/usr/bin/python3
i = ord('a')

while (i <= ord('z')):
    if (chr(i) != 'e' and chr(i) != 'q'):
        print(chr(i), end="")
    i += 1
