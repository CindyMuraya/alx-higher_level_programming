#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """represents BaseGeometry"""

    def area(self):
        """area is not implemented."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a parameter as an integer

        Args:
            name (str): name of the parameter
            value (int): the parameter to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
