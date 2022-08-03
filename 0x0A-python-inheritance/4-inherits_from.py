#!/usr/bin/python3
"""defines a function that checks if an onject is inherited"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj (any): object to check
        a_class (type): the class to match the type of obj to

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        Otherwise - False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
