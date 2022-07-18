#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format()

    Args:
        value (int): integer to print; can be any type

    Returns:
        True if value has been correctly printed - the value is an integer
        Otherwise - false
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
