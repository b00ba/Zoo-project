# -*- coding: utf-8 -*-
"""
le main de mon projet
"""
from sample.animal import Animal
from sample.animals.bird import Bird
from sample.animals.mammal import Mammal


def test_animal_1():
    """
        fonction pour tester Animal
    """
    mon_animal = Animal("zarafa")
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal.set_attack_point(5)
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal.set_life_point(100)
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal.set_voice("ba3aaaaw")
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal.eat()
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal.eat(20)
    print("TO_STRING: " + mon_animal.to_string())
    mon_animal_2 = Animal("7allouf")
    print("TO_STRING: " + mon_animal_2.to_string())
    mon_animal_2.set_life_point(200)
    mon_animal_2.set_attack_point(30)
    print("TO_STRING: " + mon_animal_2.to_string())
    mon_animal_2.set_voice("Grrrrrrrr")
    print("TO_STRING: " + mon_animal_2.to_string())
    mon_animal_2.eat(40)
    print("TO_STRING: " + mon_animal_2.to_string())
    mon_animal_2.attack(mon_animal)
    print("TO_STRING: " + mon_animal_2.to_string())
    print("TO_STRING: " + mon_animal.to_string())
    print("Execution de str():")
    print(str(mon_animal))
    print("print(mon_animal):")
    print(mon_animal)

def test_mammal_1():
    """
    module de test mammal
    """
    mon_mammal = Mammal("mammal")
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal.set_attack_point(5)
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal.set_life_point(100)
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal.set_voice("ba3aaaaw")
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal.eat()
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal.eat(20)
    print("TO_STRING: " + mon_mammal.to_string())
    mon_mammal_2 = Mammal("bird2")
    print("TO_STRING: " + mon_mammal_2.to_string())
    mon_mammal_2.set_life_point(200)
    mon_mammal_2.set_attack_point(30)
    print("TO_STRING: " + mon_mammal_2.to_string())
    mon_mammal_2.set_voice("Grrrrrrrr")
    print("TO_STRING: " + mon_mammal_2.to_string())
    mon_mammal_2.eat(40)
    print("TO_STRING: " + mon_mammal_2.to_string())
    mon_mammal_2.attack(mon_mammal)
    print("TO_STRING: " + mon_mammal_2.to_string())
    print("TO_STRING: " + mon_mammal.to_string())
    print("Execution de str():")
    print(str(mon_mammal))
    print("print(mon_mammal):")
    print(mon_mammal)


def test_animal_move():
    """
        module de test pour verifier l'exception move()
    """
    my_animal_1 = Animal(name="my_animal_move")
    print(my_animal_1.to_string())
    try:
        my_animal_1.move()
    except NotImplementedError:
        print("animal is OK ! ")


def test_animal_speak():
    """
        module de test pour verifier l'exception speak()
    """
    my_animal_1 = Animal(name="my_animal_speak")
    print(my_animal_1.to_string())
    try:
        my_animal_1.speak()
    except NotImplementedError:
        print("animal is OK ! ")

def test_bird():
    """
    module de test bird
    """
    my_bird_1 = Bird(name="my_bird_1")
    print(str(my_bird_1))
    my_bird_1.move()


def test_mammal():
    """
        module de test mammal
    """
    my_mammal_1 = Mammal(name="my_mammal_1")
    print(str(my_mammal_1))
    my_mammal_1.move()




if __name__ == "__main__":
   test_animal_1() 
