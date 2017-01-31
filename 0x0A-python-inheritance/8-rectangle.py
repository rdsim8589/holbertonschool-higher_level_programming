#!/usr/bin/python3
"""
This is the base_geometry class
"""


class BaseGeometry:
    """
    This class doesn't do anything
    """
    def area(self):
        """
        returns the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    this is the Rectangle the class
    """
    def __init__(self, width, height):
        """
        the init of the class
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__height = height
        self.__width = width
