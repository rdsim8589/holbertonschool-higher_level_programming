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
    list_of_list = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []
    or not isinstance(matrix[0], list):
        raise TypeError(list_of_list)
    if not isinstance(div, int or float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    cpy_mtx = []
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(list_of_list)
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        tmp_row = []
        for number in row:
            if type(number) != int and type(number) != float:
                raise TypeError(list_of_list)
            tmp_row.append(round(number/div, 2))
        cpy_mtx.append(tmp_row)
    return cpy_mtx
