#!/usr/bin/python3
"""
Task 1 - matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """function that divide all the values of the matrix"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err_msg)
    """if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    results_matrix = []
    for listas in matrix:
        if type(listas) != list:
            raise TypeError(err_msg)
        if len(listas) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        c_resList = []
        for valor in listas:
            if type(valor) != int and type(valor) != float:
                raise TypeError(err_msg)
            c_resList.append(round(valor/div, 2))
        results_matrix.append(c_resList)
    return results_matrix
