#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Module de test de la classe Enclosure
"""

import pytest
from sample.animal import Animal
from sample.enclosure import Enclosure
from sample.animals.mammals.dog import Dog
from sample.animals.mammals.cat import Cat
from sample.zoo import Zoo


def test_set_name():
    """
    test setteur de name
    """
    animal1 = Animal()
    test_enclosure = Enclosure("Test", [animal1])
    test_zoo = Zoo("zoo", [test_enclosure])
    assert test_zoo.set_name() == 0
    test_zoo2 = Zoo("ok", [])
    assert test_zoo2.set_name(520) == 1


def test_get_name():
    """
    getteur de name
    """
    enco = Enclosure("enclos")
    test_zoo = Zoo("Test", [enco])
    assert test_zoo.get_name() == "Test"


def test_set_list_enclosure():
    """
    test setteur de list animaux
    """
    ma_liste = []
    animal1 = Animal("test1")
    enclos = Enclosure("Test", [animal1])
    ma_liste.append(enclos)
    test_zoo1 = Zoo("zoo", [])
    assert test_zoo1.set_list_enclosure(ma_liste) == 0
    test_zoo2 = Zoo("ok", [])
    assert test_zoo2.set_list_enclosure(520) == 1


def test_get_list_enclosure():
    """
    test getteur de liste enclosure
    """
    enclo1 = Enclosure("test1")
    enclo2 = Enclosure("test2")
    enclo3 = Enclosure("test3")
    test_zoo = Zoo("test", [enclo1, enclo2, enclo3])
    assert test_zoo.get_list_enclosure() == [enclo1, enclo2, enclo3]

def test_to_string():    
    """
    fonction to_string_zoo
    """
    test_animal1 = Dog("Fox", 5, 10, "testing")
    test_animal2 = Cat("Miao", 10, 10, "testing2")
    test_enclosure1 = Enclosure("enclos-0", [test_animal1,test_animal2])
    test_animal = Dog("Rex", 5, 10, "testing2", 4)
    test_animal3 = Cat("kitty", 5, 10, "testing2", 4)
    test_enclosure2 = Enclosure("enclos-1", [test_animal, test_animal3])
    test_zoo = Zoo("zomba", [test_enclosure1, test_enclosure2])
    msg = "Le zoo appelé zomba contient : \n" + str(test_enclosure1.to_string()+"\n") + str(test_enclosure2.to_string()+"\n")
    assert test_zoo.to_string() == msg

def test_feed_all():
    """
    test de la fonction feed_all zoo
    """
    test_animal1 = Animal("Test1", 5, 10, "testing1")
    test_animal2 = Animal("Test2", 10, 10, "testing2")
    test_enclosure1 = Enclosure("test", [test_animal1, test_animal2])
    test_animal3 = Dog("Fox", 15, 10, "testing")
    test_animal4 = Cat("Miao", 20, 10, "testing2")
    test_enclosure2 = Enclosure("enclos-0", [test_animal3,test_animal4])
    test_zoo = Zoo("zomba", [test_enclosure1, test_enclosure2])
    test_zoo.feed_all(5)
    assert test_animal1.get_life_point() == 10
    assert test_animal2.get_life_point() == 15
    assert test_animal3.get_life_point() == 20
    assert test_animal4.get_life_point() == 25

def test_all_speaking():
    """
    test de la fonction feed_all_speaking zoo
    """
    test_animal1 = Dog("Test1", 5, 10, "hab-hab")
    test_animal2 = Dog("Test2", 10, 10, "grrr")
    enclo1 = Enclosure("test", [test_animal1, test_animal2])
    test_animal3 = Dog("Fox", 15, 10, "miao")
    test_animal4 = Cat("Miao", 20, 10, "myiiiao")
    enclo2 = Enclosure("enclos-0", [test_animal3,test_animal4])
    test_zoo = Zoo("zomba", [enclo1, enclo2])
    assert test_zoo.all_speaking() == str(enclo1.all_speaking()+"\n") + str(enclo2.all_speaking()+"\n")

def test_create_enclosure():
    """
    permet de tester la création d'un enclos
    """
    test_animal1 = Dog("Test1", 5, 10, "hab-hab")
    test_animal2 = Dog("Test2", 10, 10, "grrr")
    enclo1 = Enclosure("test", [test_animal1, test_animal2])
    test_zoo = Zoo("zomba", [enclo1])
    test_zoo.create_enclosure("zomba")
    assert len(test_zoo.get_list_enclosure()) == 2
