#!/usr/bin/python3

"""This module defines a function print_square"""

def print_square(size):
    """This function prints a square with the character #

    Args:
        size (int): The size of the square to be printed

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        TypeError: If size is a float and is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
