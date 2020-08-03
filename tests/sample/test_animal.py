#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe Animal
"""
import pytest
from sample.animal import Animal

def test_to_string():
    """
        Test de la fonction to_string
    """
    test_animal = Animal("Test", 5, 10, "testing")
    assert test_animal.to_string() == "Test a 5 PV et 10 PA et je dis testing"

def test_attack():
    """
        Test de la fonction attack
    """
    test_attacking = Animal("Test", 5, 2, "KILL")
    test_victim = Animal("Test2", 10, 1, "HELP")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8

def test_eat():
    """
        Test de la fonction eat
    """
    test_animal = Animal(
        name="Test",
        life_point=5,
        attack_point=10,
        voice="testing"
        )
    test_animal.eat()
    assert test_animal.get_life_point() == 10
    test_animal.eat(energy=50)
    assert test_animal.get_life_point() == 60


def test_move():
    """
        Test de la fonction move
    """
    with pytest.raises(NotImplementedError):
        test_animal = Animal("Test", 5, 10, "testing")
        test_animal.move()


def test_speak():
    """
        Test de la fonction speak
    """
    test_animal = Animal("Test", 5, 10, "testing")
    try:
        test_animal.speak()
    except NotImplementedError:
        print("NOtImplementedError a été déclenché dans test animal")


def test_set_name():
    """
            test set name
    """
    test_animal = Animal("Test")
    assert test_animal.set_name() == 0
    test_animal_2 = Animal("ok")
    assert test_animal_2.set_name(520) == 1


def test_get_name():
    """
    test get de name
    """
    test_animal = Animal("Test")
    assert test_animal.get_name() == "Test"

def test_get_life_point():
    """
    test getteur point de vie
    """
    test_animal = Animal("Test", 5, 10, "testing")
    assert test_animal.get_life_point() == 5

def test_get_attack_point():
    """
    test getteur points d'attack
    """
    test_animal = Animal("Test", 5, 10, "testing")
    assert test_animal.get_attack_point() == 10

def test_set_voice():
    """
    test setteur de voix
    """
    test_animal = Animal("Test", 5, 10, "testing")
    assert test_animal.set_voice(voice="testing_2") == 0
    assert test_animal.set_voice(voice=201) == 1

def test_get_voice():
    """
    test getteur de voix
    """
    test_animal = Animal("Test", 5, 10, "voice_1")
    assert test_animal.get_voice() == "voice_1"
