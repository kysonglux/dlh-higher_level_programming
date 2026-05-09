#!/usr/bin/env python3
"""how to use pickle"""


import pickle
import os


class CustomObject:
    """ create CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name should be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age should be an integer")
        self._age = value

    @property
    def is_student(self):
        return self._is_student

    @is_student.setter
    def is_student(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_student should be a boolean")
        self._is_student = value

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        if not os.path.exists(filename):
            return None
        with open(filename, "rb") as f:
            return pickle.load(f)
