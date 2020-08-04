#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe Animal
"""

from sample.animals.mammal import Mammal


def test_move(capsys):
    """
        Test de la fonction move
    """
    test_mammal = Mammal("Test", 8, 6, "testing", 2)
    test_mammal.move()
    captured = capsys.readouterr()
    assert captured.out == "Test is walking\n"

def test_to_string():
    """
        Test de la fonction to_string
    """
    test_mammal = Mammal("Test", 5, 10, "testing", 4)
    expect_result = "Test a 5 PV et 10 PA et je dis testing et j'ai 4 pattes"
    assert expect_result == test_mammal.to_string()

def test_get_nb_of_legs():
    """
    getteur pour nombre de pattes
    """
    test_mammal = Mammal("Test", 5, 10, "testing", 4)
    expect_result = 4
    assert expect_result == test_mammal.get_nb_of_legs()

def test_set_nb_of_legs():
    """
    test de setteur de nb_of_legs
    """
    test_mammal = Mammal(
        name="Test",
        life_point=5,
        attack_point=10,
        voice="testing",
        nb_of_legs=4
        )
    test_mammal.set_nb_of_legs(nb_of_legs=4)
    assert test_mammal.get_nb_of_legs() == 4
    assert test_mammal.set_nb_of_legs(nb_of_legs="nb_of_legs") == 1
