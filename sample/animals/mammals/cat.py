# -*- coding: utf-8 -*-
"""
classe chat qui hérite de la classe mammal
"""
# pylint: disable=redefined-outer-name
from sample.animals.mammal import Mammal


class Cat(Mammal):
    """
    classe chat hérite de Mammal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=100, attack_point=25,
                 voice="Cat-myaw", nb_of_legs=4):
        """
        fonction pour instancier notre classe Chat
        """
        super().__init__(name=name, life_point=life_point,
                         attack_point=attack_point, voice=voice,
                         nb_of_legs=nb_of_legs)
