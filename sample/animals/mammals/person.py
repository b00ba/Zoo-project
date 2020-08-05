# -*- coding: utf-8 -*-
"""
classe person qui hérite de la classe mammal
"""
# pylint: disable=redefined-outer-name
from sample.animals.mammal import Mammal


class Person(Mammal):
    """
    classe Personne hérite de Mammal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", first_name="", life_point=100,
                 attack_point=100, voice="Hello world", nb_of_legs=2):
        """
        fonction pour instancier notre classe Person
        """
        super().__init__(name=name, life_point=life_point, attack_point=attack_point,
                         voice=voice, nb_of_legs=nb_of_legs)
        self.__first_name = None
        self.set_first_name(first_name=first_name)

    def get_first_name(self):
        """
        fonction qui return le first name
        """
        return self.__first_name

    def set_first_name(self, first_name=""):
        """
        setteur de first name
        """
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("type of first_name is not STR")


    def to_string(self):
        """
        une autre fonction qui retourne un msg complet
        """
        basic = super().to_string()
        nom = "Monsieur {} ".format(self.get_first_name())
        return "{}{} ".format(nom, basic)
