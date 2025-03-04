## person.py
from abc import ABC

# Abstract class Person
class Person(ABC):
    def __init__(self, name, age):
        self._name = name  # Encapsulation
        self._age = age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
