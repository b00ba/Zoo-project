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


def test_set_name():
    """
    test setteur de name
    """
    animal1 = Animal()
    test_enclosure = Enclosure("Test", [animal1])
    assert test_enclosure.set_name() == 0
    test_enclosure_2 = Enclosure("ok", [])
    assert test_enclosure_2.set_name(520) == 1


def test_get_name():
    """
    getteur de name
    """
    animal1 = Animal()
    test_enclosure = Enclosure("Test", [animal1])
    assert test_enclosure.get_name() == "Test"


def test_set_list_animaux():
    """
    test setteur de list animaux
    """
    ma_liste = []
    animal1 = Animal("Test", 5, 10, "testing")
    ma_liste.append(animal1)
    test_enclosure = Enclosure("Test", [])
    assert test_enclosure.set_list_animaux(ma_liste) == 0
    test_enclosure_2 = Enclosure("ok", [])
    assert test_enclosure_2.set_list_animaux(520) == 1


def test_get_list_animaux():
    """
    test getteur de name
    """
    animal1 = Animal("test1")
    animal2 = Animal("test2")
    animal3 = Animal("test3")
    test_enclosure = Enclosure("test", [animal1, animal2, animal3])
    assert test_enclosure.get_list_animaux() == [animal1, animal2, animal3]


def test_to_string():
    """
    fonction to_string
    """
    test_animal1 = Dog("Fox", 5, 10, "testing")
    test_animal2 = Cat("Miao", 10, 10, "testing2")
    test_enclosure = Enclosure("enclos-1", list_animaux=[test_animal1,test_animal2])
    msg = "L enclos appelé enclos-1 contient :\nFox a 5 PV et 10 PA et je dis testing et j'ai 4 pattes\nMiao a 10 PV et 10 PA et je dis testing2 et j'ai 4 pattes\n"
    assert test_enclosure.to_string() == msg

def test_add_animal():
    """
    test:permet d’ajouter un Animal dans la liste
    """
    test_enclosure = Enclosure("test")
    test_animal1 = Animal("Test1", 5, 10, "testing2")
    test_enclosure.add_animal(test_animal1)
    assert len(test_enclosure.get_list_animaux()) == 1


def test_remove_animal():
    """
    test:permet de retirer un Animal de la liste en fonction de sa position dans la liste
    """
    test_animal1 = Animal("Test1", 5, 10, "testing1")
    test_animal2 = Animal("Test2", 10, 10, "testing2")
    test_enclosure = Enclosure("test", [test_animal1, test_animal2])
    test_enclosure.remove_animal(1)
    assert len(test_enclosure.get_list_animaux()) == 1


def test_all_attacking():
    """
    test:permet de retirer un Animal de la liste en fonction de sa position dans la liste
    """
    dog_0 = Dog("Dog-0", 5, 10, "Voice-Dog-0")
    dog_1 = Dog("Dog-1", 5, 10, "Voice-Dog-1")
    dog_2 = Dog("Dog-2", 5, 10, "Voice-Dog-2")
    dog_3 = Dog("Dog-3", 5, 10, "Voice-Dog-3")
    dog_4 = Dog("Dog-4", 5, 10, "Voice-Dog-4")
    dog_5 = Dog("Dog-5", 5, 10, "Voice-Dog-5")
    dog_6 = Dog("Dog-6", 5, 10, "Voice-Dog-6")
    dog_7 = Dog("Dog-7", 5, 10, "Voice-Dog-7")

    enclosure_0 = Enclosure(
        "Enclos-0",
        [
            dog_0,
            dog_1,
            dog_2,
            dog_3,
            dog_4,
            dog_5,
            dog_6,
            dog_7
        ]
    )
    assert enclosure_0.all_attacking() == 0
    


def test_feed_all():
    """
    test:permet de retirer un Animal de la liste en fonction de sa position dans la liste
    """
    test_animal1 = Animal("Test1", 5, 10, "testing1")
    test_animal2 = Animal("Test2", 10, 10, "testing2")
    test_enclosure = Enclosure("test", [test_animal1, test_animal2])
    test_enclosure.feed_all()
    assert test_animal1.get_life_point() == 10
    assert test_animal2.get_life_point() == 15
    

def test_all_speaking():
    """
    test: permet de retirer un Animal de la liste en fonction de sa position dans la liste
    """
    test_animal3 = Dog("Test3", 5, 10, "testing3")
    test_animal4 = Cat("Test4", 10, 10, "testing4")
    test_enclosure = Enclosure("test", [test_animal4, test_animal3])
    assert test_enclosure.all_speaking() == "l'animal Test4 dit :testing4\nl'animal Test3 dit :testing3\n"
