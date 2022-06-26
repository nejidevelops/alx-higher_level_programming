#!/usr/bin/python3
"""Defines a method for adding two integers"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): First operand
        b (int): Second operand

    Raises:
        TypeError: If either or both of the operands is not an integer
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return (a + b)
