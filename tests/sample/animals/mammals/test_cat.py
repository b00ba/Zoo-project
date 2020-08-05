#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe pigeon
"""

from sample.animals.mammals.cat import Cat

def test_speak():
    """
    fonction qui fait parler l animal
    """
    chat = Cat("chat", 5, 2, "miaw")
    chat.speak()

def test_attack():
    """
    fonction pour attacker un autre animal
    """
    test_attacking = Cat("Test", 5, 2, "KILL")
    test_victim = Cat("Test2", 10, 1, "HELP")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8
