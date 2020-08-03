# -*- coding: utf-8 -*-
"""
high level support for doing this and that.
"""
from sample.animal import Animal


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




if __name__ == "__main__":
   test_animal_1() 
