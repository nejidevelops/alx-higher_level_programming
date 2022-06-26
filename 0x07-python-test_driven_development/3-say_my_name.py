#!/usr/bin/python3

"""Defines a function say_my_name"""

def say_my_name(first_name, last_name=""):
    """Prints my name is <first_name> <last_name>

    Args:
        first_name (str): The first name to be entered.
        last_name (str): The second name to be entered.

    Raises:
        TypeError: If either argument to the function is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
