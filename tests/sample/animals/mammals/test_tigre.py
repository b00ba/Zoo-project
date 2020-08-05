#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe pigeon
"""

from sample.animals.mammals.tigre import Tigre

def test_speak():
    """
    fonction qui fait parler l animal
    """
    tigre_1 = Tigre("tigre_1", 5, 2, "KILL")
    tigre_1.speak()

def test_attack():
    """
    fonction pour attacker un autre animal
    """
    test_attacking = Tigre("Test", 5, 2, "KILL")
    test_victim = Tigre("Test2", 10, 1, "HELP")
    test_attacking.attack(test_victim)
    assert test_victim.get_life_point() == 8
