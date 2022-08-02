#!/usr/bin/python3
"""defines a function for JSON serialization of an object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""

    return obj.__dict__
