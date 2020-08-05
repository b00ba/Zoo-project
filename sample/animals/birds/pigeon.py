# -*- coding: utf-8 -*-
"""
classe pigeon qui hérite de la classe bird
"""
# pylint: disable=redefined-outer-name
from sample.animals.bird import Bird


class Pigeon(Bird):
    """
    classe Pigeon hérite de bird
    """
    # pylint: disable=too-many-arguments
    def __init__(self, name="", life_point=100, attack_point=15,
                 voice="ghargher", nb_of_wings=2):
        """
        fonction pour instancier notre classe Eagle
        """
        super().__init__(name=name, life_point=life_point, attack_point=attack_point,
                         voice=voice, nb_of_wings=nb_of_wings)
