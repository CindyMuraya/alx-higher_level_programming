#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new student

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved

        Args:
            attrs (list): attributes to be represented
        """

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
