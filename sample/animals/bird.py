# -*- coding: utf-8 -*-
"""
class bird qui hérite de la classe animal
"""
# pylint: disable=redefined-outer-name
from sample.animal import Animal


class Bird(Animal):
    """
       class bird qui hérite de la classe animal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=90, attack_point=1,
                 voice="ziwziw", nb_of_wings=2):
        """
        fonction pour instancier notre classe Bird
        """
        super().__init__(name=name, life_point=life_point,
                         attack_point=attack_point, voice=voice)
        self.__nb_of_wings = None
        self.set_nb_of_wings(nb_of_wings)

    def set_nb_of_wings(self, nb_of_wings):
        """
        setteur pour nombre de aile
        """
        if isinstance(nb_of_wings, int):
            self.__nb_of_wings = nb_of_wings
            return 0
        print("type of nb_of_wings is not INT")
        return 1

    def get_nb_of_wings(self):
        """
        getteur pour nombre de aile
        """
        return self.__nb_of_wings

    def _fly(self):
        """
        fonction pour faire voler l'animal et utilisée par la fonction move()
        """
        print("{} is flying".format(self.get_name()))

    def move(self):
        """
        cette fonction est utilisée par la fonction move()
        """
        self._fly()

    def to_string(self):
        """
        c'est la meme fonction to_string
        """
        return super().to_string() + " et j'ai " + str(self.get_nb_of_wings()) + " ailes"

    def speak(self):
        """
        cette fonction pour parler
        """
        return "l'animal " + super().get_name() + " dit :" + str(self.get_voice())
