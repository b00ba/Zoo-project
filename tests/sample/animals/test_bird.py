#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Module de test de la classe Animal
"""

from sample.animals.bird import Bird

def test_move(capsys):
    """
        Test de la fonction move
    """
    test_bird = Bird("Test", 5, 10, "testing", 2)
    test_bird.move()
    captured = capsys.readouterr()
    assert captured.out == "Test is flying\n"

def test_to_string():
    """
        Test de la fonction to_string
    """
    test_bird = Bird("Test", 5, 10, "testing", 2)
    expect_result = "Test a 5 PV et 10 PA et je dis testing et j'ai 2 ailes"
    assert expect_result == test_bird.to_string()

def test_get_nb_of_wings():
    """
    getteur pour nombre de aile
    """
    test_bird = Bird("Test", 5, 10, "testing", 2)
    expect_result = 2
    assert expect_result == test_bird.get_nb_of_wings()

def test_set_nb_of_wings():
    """
    test pour setteur nombre de aile
    """
    test_bird = Bird(
        name="Test",
        life_point=5,
        attack_point=10,
        voice="testing",
        nb_of_wings=2
        )
    test_bird.set_nb_of_wings(nb_of_wings=2)
    assert test_bird.get_nb_of_wings() == 2
    assert test_bird.set_nb_of_wings(nb_of_wings="nb_of_wings") == 1
