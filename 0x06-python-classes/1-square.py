#!/usr/bin/python3
"""
This module defines the Square class.
It includes a private instance attribute 'size' and supports instantiation with size.
"""

class Square:
    """
    A class that defines a square by its size.

    Attributes:
    size (int): The size of a side of the square.

    The size of the square is a crucial attribute that is kept private to control
    its access and modification.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
        size (int): The size of a side of the square.
        """
        self.__size = size
