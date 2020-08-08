#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
high level support for doing this and that.
"""
# pylint: disable=redefined-outer-name
from sample.enclosure import Enclosure


class Zoo:
    """
    class Enclosure
    """
    def __init__(self, name, list_enclosure=list):
        self.__name = None
        self.__list_enclosure = []
        self.set_name(name)
        self.set_list_enclosure(list_enclosure)

    def set_name(self, name=""):
        """
        setteur de nom de zoo
        """
        if isinstance(name, str):
            self.__name = name
            return 0
        print("le type n'est pas STR")
        return 1

    def get_name(self):
        """
        getteur de name de zoo
        """
        return self.__name

    def set_list_enclosure(self, list_enclosure):
        """
            setteur de liste enclosure
        """
        if isinstance(list_enclosure, list):
            self.__list_enclosure = list_enclosure
            return 0
        print("type of list is not LIST")
        return 1

    def get_list_enclosure(self):
        """
        getteur de name
        """
        return self.__list_enclosure

    def to_string(self):
        """
        fonction to_string
        """
        msg = "Le zoo appelé %s contient : \n" % (self.get_name())
        output_string = ""
        for enclo in self.get_list_enclosure():
            output_string += str(enclo.to_string()+"\n")
        return msg + str(output_string)

    def feed_all(self, energy=5):
        """
        permet de faire parler tous les animaux de zoo
        """
        if len(self.__list_enclosure) > 0:
            for enclo in self.__list_enclosure:
                enclo.feed_all(energy=energy)

    def all_speaking(self):
        """
        permet de faire parler tous les animaux de zoo
        """
        output_speak = ""
        for enclo in self.get_list_enclosure():
            output_speak += str(enclo.all_speaking()+"\n")
        return str(output_speak)

    def create_enclosure(self, name):
        """
        permet de créer un enclos
        """
        for enclos in self.__list_enclosure:
            if enclos.get_name() == name:
                return None
            nvenclos = Enclosure(name, [])
            self.__list_enclosure.append(nvenclos)
            return nvenclos

    def all_attacking(self):
        """
        permet de faire attaquer tous les animaux de tous les enclos
        """
        if self.__list_enclosure:
            for enclo in self.get_list_enclosure():
                enclo.all_attacking()
