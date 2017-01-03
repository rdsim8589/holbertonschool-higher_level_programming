#Assignment for the 0x00-python-hello_world project

##0-run
Shell script that runs a Python script.
the Python file name will be saved in the environment variable $PYFILE

##1-run_inline
Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE

##2-print.py
Python script that prints exactly "\"Programming is like building a multilingual puzzle, followed by a new line."

##3-print_number.py
Python script that prints "98 Battery street"

##4-print_float.py
Python script that print the float stored in the variable number with a precision of 2 digits.

##5-print_string.py
Python scrip that print 3 times a string stored in the variable str, followed by its first 9 characters.

##6-concat.py
Python script that print Welcome to Holberton School!

##7-edges.py
Python script that prints the first 3 characters, last 2 characters, and the all the characers expect the first and last character

##8-concat_edges.py
Python script that print object-oriented programming with Python, followed by a new line.

##9-easter_egg.py
Python script that prints out the poem "The Zen of Python", by TimPeters

##100-write.py
 a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19
+ Use the function write from the sys module
+ You are not allowed to use print
+ You script should print to stderr
    - Your script should exit with the status code 1

##101-compile
A shell script that compiles a Python script file.
The Python file name will be stored in the environment variable $PYFILE
The output filename has to be $PYFILEc (ex: PYFILE=my_main.py => my_main.pyc)

##102-magic_calculation.py
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
