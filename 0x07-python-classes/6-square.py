#!/usr/bin/python3
"""
This is the Square module.

The Square module contains the Square class
"""


class Square:
    """ This is the Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """ The __init__ method
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position setter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ returns the current square area
        """
        size = self.__size
        return(size ** 2)

    def my_print(self):
        """ prints a square of #
        """
        size = self.__size
        position = self.__position
        if size == 0:
            print()
        else:
            for i in range(position[1]):
                print()
            print_sq = []
            for i in range(size):
                row = []
                for i in range(size + position[0]):
                    if i < position[0]:
                        row.append(" ")
                    else:
                        row.append("#")
                print_sq.append("".join(row))
            print("\n".join(print_sq))
