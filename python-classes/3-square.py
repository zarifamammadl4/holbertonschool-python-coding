#!/usr/bin/python3
"""Module that defines a Square class with getter and setter."""


class Square:
    """Class that defines a square with size validation and area method."""

    def __init__(self, size=0):
        """Initialize the square using the size setter."""
        self.size = size  # uses setter to validate

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
