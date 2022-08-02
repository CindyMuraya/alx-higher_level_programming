#!/usr/bin/python3
"""defines a function that writes a string to a text file"""


def write_file(filename="", text=""):

    """writes a string to a text file (UTF8)

    Args:
        filename (str): name of the file to be written
        text (str): the text to be written to the file

    Returns:
        the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
