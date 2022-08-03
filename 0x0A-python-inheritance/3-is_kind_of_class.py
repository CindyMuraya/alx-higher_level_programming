#!/usr/bin/python3
"""defines a function that checks for class and inherited class objects"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class

    Args:
        obj (any): object to check
        a_class (type): the class to match the type of obj to

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    return False
