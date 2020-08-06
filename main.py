# -*- coding: utf-8 -*-
"""
high level support for doing this and that.
"""
from sample.animal import Animal
from sample.zoo import Zoo
from sample.enclosure import Enclosure
from sample.animals.bird import Bird
from sample.animals.mammal import Mammal
from sample.animals.mammals.tigre import Tigre
from sample.animals.mammals.cat import Cat
from sample.animals.mammals.dog import Dog
from sample.animals.birds.eagle import Eagle
from sample.animals.birds.pigeon import Pigeon


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


def test_bird_1():
    """
    module de test bird
    """
    mon_bird = Bird("oiseau")
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird.set_attack_point(5)
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird.set_life_point(100)
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird.set_voice("ba3aaaaw")
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird.eat()
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird.eat(20)
    print("TO_STRING: " + mon_bird.to_string())
    mon_bird_2 = Bird("oiseau2")
    print("TO_STRING: " + mon_bird_2.to_string())
    mon_bird_2.set_life_point(200)
    mon_bird_2.set_attack_point(30)
    print("TO_STRING: " + mon_bird_2.to_string())
    mon_bird_2.set_voice("Grrrrrrrr")
    print("TO_STRING: " + mon_bird_2.to_string())
    mon_bird_2.eat(40)
    print("TO_STRING: " + mon_bird_2.to_string())
    mon_bird_2.attack(mon_bird)
    print("TO_STRING: " + mon_bird_2.to_string())
    print("TO_STRING: " + mon_bird.to_string())
    print("Execution de str():")
    print(mon_bird.to_string())
    print("print(mon_bird):")
    print(mon_bird.to_string())


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


def verif_cri_animaux():
    """
        module pour verifier que chaque animal a un crie différent
    """
    tigre_1 = Tigre("Test4", 10, 10, "testing4", 4)
    tigre_1.speak()


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


def test_all_attacking():
    """
    test:permet de faire attacker les animaux
    """
    dog_0 = Dog("Dog-0", 5, 10, "Voice-Dog-0")
    dog_1 = Dog("Dog-1", 5, 20, "Voice-Dog-1")
    dog_2 = Dog("Dog-2", 5, 10, "Voice-Dog-2")
    dog_3 = Dog("Dog-3", 50, 10, "Voice-Dog-3")
    dog_4 = Dog("Dog-4", 5, 20, "Voice-Dog-4")
    dog_5 = Dog("Dog-5", 15, 10, "Voice-Dog-5")
    dog_6 = Dog("Dog-6", 50, 20, "Voice-Dog-6")
    dog_7 = Dog("Dog-7", 5, 30, "Voice-Dog-7")

    enclosure_0 = Enclosure(
        "Enclos-0",
        [
            dog_0,
            dog_1,
            dog_2,
            dog_3,
            dog_4,
            dog_5,
            dog_6,
            dog_7
        ]
    )
    print("=== Before attack:")
    print(str(enclosure_0.to_string()))
    print("=== After attack:")
    enclosure_0.all_attacking()
    print(str(enclosure_0.to_string()))


def enclos_to_string():
    """
    fonction to_string
    """
    test_animal1 = Dog("Rex", 5, 10, "testing2", 4)
    test_animal2 = Cat("kitty", 5, 10, "testing2", 4)
    test_enclosure = Enclosure("enclos-1", list_animaux=[test_animal1, test_animal2])
    print(str(test_enclosure.to_string()))

def test_all_speaking():
    """
    test all speaking
    """
    test_animal1 = Dog("Test1", 5, 10, "testing1")
    test_animal2 = Cat("Test2", 10, 10, "testing2")
    test_animal3 = Pigeon("Test3", 5, 10, "testing3")
    test_animal4 = Eagle("Test4", 10, 10, "testing4")
    test_enclosure = Enclosure("test", [test_animal1, test_animal2, test_animal3, test_animal4])
    print(str(test_enclosure.all_speaking()))

def test_feeding_enclo():
    """
    fonction test_feeding_enclo
    """
    test_animal1 = Animal("Test1", 5, 10, "testing1")
    test_animal2 = Animal("Test2", 10, 10, "testing2")
    test_enclosure = Enclosure("test", [test_animal1, test_animal2])
    test_enclosure.feed_all(50)
    print(test_animal1.get_life_point())
    print(test_animal2.get_life_point())

def test_feeding_zoo():
    """
    fonction test_feeding_zoo
    """
    test_animal = Dog("Rex", 17, 10, "testing2", 4)
    test_animal5 = Cat("kitty", 8, 10, "testing2", 4)
    test_enclosure1 = Enclosure("enclos-1", [test_animal, test_animal5])
    test_animal1 = Dog("Test1", 5, 10, "testing1")
    test_animal2 = Cat("Test2", 25, 10, "testing2")
    test_animal3 = Pigeon("Test3", 15, 10, "testing3")
    test_animal4 = Eagle("Test4", 10, 10, "testing4")
    test_enclosure2 = Enclosure("test", [test_animal1, test_animal2, test_animal3, test_animal4])
    test_zoo = Zoo("zomba", [test_enclosure1, test_enclosure2])
    test_zoo.feed_all(100)
    print(test_animal.get_life_point())
    print(test_animal1.get_life_point())
    print(test_animal2.get_life_point())
    print(test_animal3.get_life_point())
    print(test_animal4.get_life_point())
    print(test_animal5.get_life_point())

def test_all_speaking_zoo():
    """
    fonction test_speaking_zoo
    """
    test_animal = Dog("Rex", 17, 10, "testing2", 4)
    test_animal5 = Cat("kitty", 8, 10, "testing2", 4)
    test_enclosure1 = Enclosure("enclos-1", list_animaux=[test_animal, test_animal5])
    test_animal1 = Dog("Test1", 5, 10, "testing1")
    test_animal2 = Cat("Test2", 25, 10, "testing2")
    test_animal3 = Pigeon("Test3", 15, 10, "testing3")
    test_animal4 = Eagle("Test4", 10, 10, "testing4")
    test_enclosure2 = Enclosure("test", [test_animal1, test_animal2, test_animal3, test_animal4])
    test_zoo = Zoo("zomba", [test_enclosure1, test_enclosure2])
    print(str(test_zoo.all_speaking()))

def test_create_enclos():
    """
    fonction test_create_enclo
    """
    test_animal6 = Dog("Test1", 5, 10, "testing1", 4)
    test_animal5 = Cat("kitty", 8, 10, "testing2", 4)
    test_enclosure1 = Enclosure("enclos", [test_animal6, test_animal5])
    test_zoo = Zoo("zoo", [test_enclosure1])
    # assert isinstance(test_zoo.create_enclosure("test123"), Enclosure)
    print(str(test_zoo.create_enclosure("enclos1")))
    print(str(test_zoo.to_string()))

def zoo_to_string():
    """
    fonction to_string
    """
    test_animal = Dog("Rex", 5, 10, "testing2", 4)
    test_animal5 = Cat("kitty", 5, 10, "testing2", 4)
    test_enclosure1 = Enclosure("enclos-1", [test_animal, test_animal5])
    test_animal1 = Dog("Test1", 5, 10, "testing1")
    test_animal2 = Cat("Test2", 10, 10, "testing2")
    test_animal3 = Pigeon("Test3", 5, 10, "testing3")
    test_animal4 = Eagle("Test4", 10, 10, "testing4")
    test_enclosure2 = Enclosure("test", [test_animal1, test_animal2, test_animal3, test_animal4])
    test_zoo = Zoo("zomba", [test_enclosure1, test_enclosure2])
    print(str(test_zoo.to_string()))


if __name__ == "__main__":
    # test_all_attacking()
    # enclos_to_string()
    # test_all_speaking()
    # verif_cri_animaux()
    # zoo_to_string()
    # test_feeding_zoo()
    # test_all_speaking_zoo()
    test_create_enclos()
