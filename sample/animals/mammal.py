# -*- coding: utf-8 -*-
"""
class mammal qui hérite de la classe animal
"""
from sample.animal import Animal


class Mammal(Animal):
    """
       class mammal qui hérite de la classe animal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=100, attack_point=11,
                 voice="Woooo", nb_of_legs=4):
        """
        fonction pour instancier notre classe Mammal
        """
        super().__init__(name, life_point, attack_point, voice)
        self.__nb_of_legs = None
        self.set_nb_of_legs(nb_of_legs)

    def set_nb_of_legs(self, nb_of_legs):
        """
        setteur de nb_of_legs
        """
        if isinstance(nb_of_legs, int):
            self.__nb_of_legs = nb_of_legs
            return 0
        print("type of nb_of_legs is not INT")
        return 1

    def get_nb_of_legs(self):
        """
        getteur de nb_of_legs
        """
        return self.__nb_of_legs

    def _walk(self):
        """
        cette fonction est utilisée par la fonction move()
        """
        print("{} is walking".format(self.get_name()))

    def move(self):
        """
        cette fonction est utilisée par la fonction move()
        """
        self._walk()

    def to_string(self):
        """
        cette fonction pour afficher les informatons
        """
        return super().to_string() + " et j'ai " + str(self.get_nb_of_legs()) + " pattes"


    def speak(self):
        """
        cette fonction pour parler
        """
        return "l'animal " + super().get_name() + " dit :" + str(self.get_voice())
