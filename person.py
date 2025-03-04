## person.py
from abc import ABC # import de la class ABC pour creer une classe abstraite en python j'ai pas tous compris a re regarder pas capter pk ABC specifiquement mais aze sa marche pas sans sa 

# Abstract class Person
class Person(ABC):  # class personne qui herite de ABC 
    def __init__(self, name, age):
        self._name = name  # Encapsulation
        self._age = age

    def get_name(self): # le petit gette pour acceder au attributs 
        return self._name
    
    def get_age(self):
        return self._age
