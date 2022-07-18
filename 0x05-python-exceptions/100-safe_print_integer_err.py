#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    
    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): integer to print; can be any type

    Returns:
        True if value has been correctly printed - the value is an integer
        Otherwise - False and prints in stderr the error precede by Exception:
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
