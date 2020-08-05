#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe pigeon
"""

from sample.animals.birds.pigeon import Pigeon

def test_speak():
    """
    fonction qui fait parler l animal
    """
    pigeon_2 = Pigeon("pigeon_2", 5, 2, "KILL")
    pigeon_2.speak()

def test_attack():
    """
    fonction pour attacker un autre animal
    """
    test_attacking = Pigeon("Test", 5, 2, "KILL")
    test_victim = Pigeon("Test2", 10, 1, "HELP")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8
