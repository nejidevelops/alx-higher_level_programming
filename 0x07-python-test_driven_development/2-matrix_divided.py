#!/usr/bin/python3
"""Defines a method that divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by an integer

    Args:
        matrix: A list of lists containing integers or floats
        div: The divisor to divide each element of the matrix

    Raises:
        TypeError: - If the matrix-elements are neither integers or floats
                   - If each row of the matrix  is not of the same size
                   - If the divisor is neither an integer nor a float
        ZeroDivisionError: If div is equal to zero

    The result of division is rounded to two decimal places.
    """
