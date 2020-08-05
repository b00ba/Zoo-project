# -*- coding: utf-8 -*-
"""
classe tigre qui hérite de la classe mammal
"""
# pylint: disable=redefined-outer-name
from sample.animals.mammal import Mammal


class Tigre(Mammal):
    """
    classe Tigre hérite de Mammal
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=90, attack_point=60,
                 voice="Tigre-waaaa", nb_of_legs=4):
        """
        fonction pour instancier notre classe tigre
        """
        super().__init__(name=name, life_point=life_point, attack_point=attack_point,
                         voice=voice, nb_of_legs=nb_of_legs)
