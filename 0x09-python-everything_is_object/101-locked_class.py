#!/usr/bin/python3
"""
Defines class with no class or object attribute
Control dynamically created instance attributes
"""


class LockedClass():
    """
    prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    """
    __slots__ = "first_name"
