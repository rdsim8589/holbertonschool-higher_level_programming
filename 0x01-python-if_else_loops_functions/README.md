#0x01-python-if_else_loops_functions/
Python - if/else, loops, functions

##0-positive_or_negative.py
The output of the program should be
+ The random number, followed by
  - if the number is greater than 0: is positive
  - if the number is 0: is zero
  - if the number is less than 0: is negative
+ followed by a new line
example:
```
$ ./0-positive_or_negative.py
-4 is negative
```

##1-last_digit.py
The output of the program should be:
+ The string Last digit of, followed by
+ the number, followed by
+ the string is, followed by
  - if the number is greater than 5: the string and is greater than 5
  - if the number is 0: the string and is 0
  - if the number is less than 6 and not 0: the string and is less than 6 and not 0
+ followed by a new line
example:
```
$ ./1-last_digit.py
>> Last digit of 4205 is 5 and is less than 6 and not 0
```

##2-print_alphabet.py
**The output of the program should be:**
+ The string Last digit of, followed by
+ the number, followed by
+ the string is, followed by
  - if the number is greater than 5: the string and is greater than 5
  - if the number is 0: the string and is 0
  - if the number is less than 6 and not 0: the string and is less than 6 and not 0
+ followed by a new line
example:
```
$ ./2-print_alphabet.py
>> abcdefghijklmnopqrstuvwxyz$
```

##3-print_alphabt.py
A program that prints the alphabet except q and e, in lowercase, not followed by a new line.
example:
```
$ ./3-print_alphabt.py
>> abcdfghijklmnoprstuvwxyz$
```

##4-print_hexa.py
A program that prints all numbers from 0 to 98 in decimal and in hexadecimal
example:
```
$ ./4-print_hexa.py
>> 0 = 0x0
>> 1 = 0x1
...
>> 97 = 0x61
>> 98 = 0x62
```

##5-print_comb2.py
a program that prints numbers from 0 to 99, seprated by a , followed by a space.
example:
```
$ ./5-print_comb2.py
>>00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```

##6-print_comb3.py
A program that prints all possible different combinations of two digits separated by , followed by a space
example:
```
$ ./6-print_comb3.py
>>01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```

##7-islower.py
A function that checks for lowercase character.
+ Prototype: def islower(c):
+ Returns True if c is lowercase
+ Returns False otherwise
example:
```
$ cat 7main.py
>> #!/usr/bin/env python3
>> islower = __import__('7-islower').islower
>>
>> print("a is {}".format("lower" if islower("a") else "upper"))
>> print("H is {}".format("lower" if islower("H") else "upper"))
>> print("A is {}".format("lower" if islower("A") else "upper"))
>> print("3 is {}".format("lower" if islower("3") else "upper"))
>> print("g is {}".format("lower" if islower("g") else "upper"))

$./7main.py
>> a is lower
>> H is upper
>> A is upper
>> 3 is upper
>> g is lower
```

##8-uppercase.py
a function that print a string in uppercase followed by a new line
example:
```
$ cat 8-main.py
>> #!/usr/bin/env python3
>> uppercase = __import__('8-uppercase').uppercase
>>
>> uppercase("holberton")
>> uppercase("Holberton School 98 Battery street")
>>
$ ./8-main.py
>> HOLBERTON
>> HOLBERTON SCHOOL 98 BATTERY STREET
```

##9-print_last_digit.py
 function that prints the last digit of a number
example:
```
$ cat 9-main.py
>> #!/usr/bin/env python3
>> print_last_digit = __import__('9-print_last_digit').print_last_digit
>>
>> print_last_digit(98)
>> print_last_digit(0)
>> r = print_last_digit(-1024)
>> print(r)
>>
$ ./9-main.py
>> 8044
```
##10-add.py
A function that adds two integers and returns the result.
example:
```
$ cat 10-main.py
>> #!/usr/bin/env python3
>> add = __import__('10-add').add
>>
>> print(add(1, 2))
>> print(add(98, 0))
>> print(add(100, -2))
>>
$ ./10-main.py
>> 3
>> 98
>> 98
```

##11-pow.py
A function that computes a to the power of b and return the value.
example:
```
$ cat 11-main.py
#!/usr/bin/env python3
>> pow = __import__('11-pow').pow
>>
>> print(pow(2, 2))
>> print(pow(98, 2))
>> print(pow(98, 0))
>> print(pow(100, -2))
>> print(pow(-4, 5))
>>
$ ./11-main.py
>> 4
>> 9604
>> 1
>> 0.0001
>> -1024
```

##12-fizzbuzz.py
A function that prints the numbers from 1 to 100 separated by a space.
+ But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
+ For numbers which are multiples of both three and five print FizzBuzz.
example:
```
$ cat 12-main.py
>> #!/usr/bin/env python3
>> fizzbuzz = __import__('12-fizzbuzz').fizzbuzz
>>
>> fizzbuzz()
>> print("")
>>
$ ./12-main.py | cat -e
>> 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
```

##100-print_tebahpla.py
a program that prints the alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
example:
```
$ ./100-print_tebahpla.py
>> zYxWvUtSrQpOnMlKjIhGfEdCbA$
```

##101-remove_char_at.py
A function that creates a copy of the string, removing the character at the position n.
```
$ cat 101-main.py
>> #!/usr/bin/env python3
>> remove_char_at = __import__('101-remove_char_at').remove_char_at
>>
>> print(remove_char_at("Holberton School", 3))
>> print(remove_char_at("Chicago", 2))
>> print(remove_char_at("C is fun!", 0))
>> print(remove_char_at("School", 10))
>> print(remove_char_at("Python", -2))
>>
$ ./101-main.py
>> Holerton School
>> Chcago
>>  is fun!
>> School
>> Python
```

##102-magic_calculation.py
Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
