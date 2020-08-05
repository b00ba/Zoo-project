#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
high level support for doing this and that.
"""
# pylint: disable=redefined-outer-name
import random


class Enclosure:
    """
    class Enclosure
    """
    def __init__(self, name, list_animaux=list):
        self.__name = None
        self.__list_animaux = []
        self.set_name(name)
        self.set_list_animaux(list_animaux)

    def set_name(self, name=""):
        """
        setteur de nom de l'enclosure
        """
        if isinstance(name, str):
            self.__name = name
            return 0
        print("type of nom is not STR")
        return 1

    def get_name(self):
        """
        getteur de name
        """
        return self.__name

    def set_list_animaux(self, list_animaux):
        """
            setteur de name
        """
        if isinstance(list_animaux, list):
            self.__list_animaux = list_animaux
            return 0
        print("type of list is not LIST")
        return 1

    def get_list_animaux(self):
        """
        getteur de name
        """
        return self.__list_animaux

    def to_string(self):
        """
        fonction to_string
        """
        msg = "L enclos appelé %s contient :\n" % (self.get_name())
        output_string = ""
        for anim in self.get_list_animaux():
            output_string += str(anim.to_string()+"\n")
        return msg + str(output_string)

    def feed_all(self, energy=5):
        """
        permet de nourrir tous les animaux de la liste
        """
        if len(self.__list_animaux) > 0:
            for anim in self.__list_animaux:
                anim.eat(energy=energy)


    def add_animal(self, anim):
        """
        permet d’ajouter un Animal dans la liste
        """
        self.__list_animaux.append(anim)

    def remove_animal(self, i):
        """
        permet de retirer un Animal de la liste en fonction de sa position dans la liste
        """
        self.__list_animaux.pop(i)

    def all_speaking(self):
        """
        permet de faire parler tous les animaux de l’enclos
        """
        output_speak = ""
        for anim in self.get_list_animaux():
            output_speak += str(anim.speak()+"\n")
        return str(output_speak)

    def dead_animals(self):
        """
        Enlève les zéros de la liste
        """
        list_copy = self.__list_animaux.copy()
        for item in list_copy:
            if item.get_life_point() <= 0:
                self.__list_animaux.remove(item)

    def all_attacking(self):
        """
        permet de faire attaquer tous les animaux un à un
        """
        for item in self.__list_animaux:
            if item.get_life_point() != 0:
                target_index = random.randint(0, len(self.__list_animaux) - 1)
                while self.__list_animaux.index(item) == target_index:
                    target_index = random.randint(0, len(self.__list_animaux) - 1)
                print(item.get_name() + " is attacking : " \
                    + self.__list_animaux[target_index].get_name())
                item.attack(self.__list_animaux[target_index])
            else:
                print(self.__list_animaux[target_index].get_name() + "est mort")
        self.dead_animals()
        return 0
