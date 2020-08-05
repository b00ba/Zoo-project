# -*- coding: utf-8 -*-
"""
classe eagle qui hérite de la classe bird
"""
# pylint: disable=redefined-outer-name
from sample.animals.bird import Bird


class Eagle(Bird):
    """
    classe Eagle hérite de bird
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=150, attack_point=20,
                 voice="waakwaak", nb_of_wings=3):
        """
        fonction pour instancier notre classe Eagle
        """
        super().__init__(name=name, life_point=life_point, attack_point=attack_point,
                         voice=voice, nb_of_wings=nb_of_wings)
