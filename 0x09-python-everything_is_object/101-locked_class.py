#!/usr/bin/python3
"""defines a class LockedClass"""


class LockedClass:
    """
    prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """
    __slots__ = ["first_name"]
