#!/usr/bin/python3
""" Create Class Square"""


class Square:
    """ about the square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        return self.__position = position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple)
            raise TypeError("position must be a tuple of 2 positive integers")
        
