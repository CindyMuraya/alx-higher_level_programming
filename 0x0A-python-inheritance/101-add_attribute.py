#!/usr/bin/python3
"""defines a function that adds a new attribute to an object if possible"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object if possible

    Args:
        obj (any): the object to add an attribute to
        att (str): the name of the attribute to add to obj
        value (any): the value of the attribute

    Raises:
        TypeError: if the object can't have new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
