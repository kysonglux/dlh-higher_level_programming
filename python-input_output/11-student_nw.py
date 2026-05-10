#!/usr/bin/python3
"""create a student class """


class Student:
    """about the student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("first name should be a string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("last name should be a string")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age should be an integer")
        self._age = value

    def to_json(self, attrs=None):
        all_attrs = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        if isinstance(attrs, list):
            return {k: v for k, v in all_attrs.items() if k in attrs}
        return all_attrs

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
