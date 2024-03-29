#!/usr/bin/python3
"""defines a function that reads a text file"""


def read_file(filename=""):
    """reads a text file (UTF8) and print its content to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
