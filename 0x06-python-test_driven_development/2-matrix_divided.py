#!/usr/bin/python3
"""
This is the "Matrix Divided" module

The Matrix Divided module supplies the simple function/
to divide all items of a matrix by an int or float
"""


def matrix_divided(matrix, div):
    """
    Returns a copy of the matrix divided by the int/float of div
    """
    cpy_mtx = []
    row_len = len(matrix[0])


    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        tmp_row = []
        for number in row:

            if type(number) != int and type(number) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            tmp_row.append(round(number/div, 2))
        cpy_mtx.append(tmp_row)
    return cpy_mtx
