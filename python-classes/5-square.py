#!/usr/bin/python3
""" Square class"""


class Square:
    """ """
    def ___init__(self, size=0):
        self__size = size
    
    @property
    def size(self):
        return self__size
    
    @size.setter
    def size(self, value):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        return self__size ** 2
    
    def my_print(self):
        print("{}".format())