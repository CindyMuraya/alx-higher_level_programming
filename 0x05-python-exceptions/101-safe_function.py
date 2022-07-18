#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """executes a function safely

    Args:
        fct: a pointer to a function
        args: argument

    Returns:
        the result of the function
        Otherwise - None, prints in stderr the error precede by Exception:
    """

    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
