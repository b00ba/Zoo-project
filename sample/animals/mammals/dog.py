# -*- coding: utf-8 -*-
"""
classe dog qui hérite de la classe mammal
"""
# pylint: disable=redefined-outer-name
from sample.animals.mammal import Mammal


class Dog(Mammal):
    """
    classe chien hérite de Mammal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=95, attack_point=35,
                 voice="habhab", nb_of_legs=4):
        """
        fonction pour instancier notre classe Dog
        """
        super().__init__(name=name, life_point=life_point, attack_point=attack_point,
                         voice=voice, nb_of_legs=nb_of_legs)
