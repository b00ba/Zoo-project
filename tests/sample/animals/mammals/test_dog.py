#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe pigeon
"""

from sample.animals.mammals.dog import Dog

def test_speak():
    """
    fonction qui fait parler l animal
    """
    chien = Dog("Rex", 5, 2, "habhab")
    chien.speak()

def test_attack():
    """
    fonction pour attacker un autre animal
    """
    test_attacking = Dog("Rex", 5, 2, "habhab")
    test_victim = Dog("Fox", 10, 1, "HELP")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8
