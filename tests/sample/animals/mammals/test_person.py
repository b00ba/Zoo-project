#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe person
"""

from sample.animals.mammals.person import Person

def test_get_first_name():
    """
    fonction pour tester get_first_name
    """
    test_person = Person("vincent", "leroy", 5, 10, "voice_1")
    assert test_person.get_first_name() == "leroy"

def set_first_name():
    """
    test setteur de first name
    """
    test_person = Person("vincent", "leroy", 5, 10, "voice_1")
    assert test_person.set_voice(voice="testing_2") == 0
    assert test_person.set_voice(voice=201) == 1

def test_speak():
    """
    fonction qui fait parler Person
    """
    test_person = Person("vincent", "leroy", 5, 10, "voice_1")
    test_person.speak()

def test_attack():
    """
    fonction pour attacker un autre animal
    """
    test_attacking = Person("vincent", "leroy", 5, 2, "voice_1")
    test_victim = Person("edward", "leclerc", 10, 1, "voice_2")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8

def test_to_string():
    """
    une autre fonction qui retourne un msg complet
    """
    per = "Monsieur leroy vincent a 5 PV et 10 PA et je dis voice_1 et j'ai 2 pattes "
    person_1 = Person("vincent", "leroy", 5, 10, "voice_1")
    assert person_1.to_string() == per
