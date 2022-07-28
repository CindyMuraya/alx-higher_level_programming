#!/usr/bin/python3
"""defines an integer addition function"""


def add_integer(a, b=98):
    """returns the addition of two integers a and b

    Float arguments are casted to integers before addition

    Raises:
        TypeError: if either of a or b is non-integer
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
