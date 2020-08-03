# -*- coding: utf-8 -*-
"""
high level support for doing this and that.
"""
# pylint: disable=redefined-outer-name
class Animal:
    """
        class animal
    """
    def __init__(
            self,
            name="",
            life_point=0,
            attack_point=0,
            voice="cri"
    ): # pylint: disable=too-many-arguments
        self.__name = None
        self.__life_point = None
        self.__attack_point = None
        self.__voice = None
        self.set_name(name)
        self.set_life_point(life_point)
        self.set_attack_point(attack_point)
        self.set_voice(voice)

    def set_name(self, name=""):
        """
            setteur de name
        """
        if isinstance(name, str):
            self.__name = name
            return 0
        print("type of name is not STR")
        return 1

    def get_name(self):
        """
        getteur de name
        """
        return self.__name

    def set_life_point(self, life_point):
        """
        setteur des point de vie
        """
        if isinstance(life_point, int):
            self.__life_point = life_point
            return 0
        print("type of name is not INT")
        return 1

    def get_life_point(self):
        """
        getteur point de vie
        """
        return self.__life_point

    def set_attack_point(self, attack_point):
        """
        setteur point d'attack
        """
        if isinstance(attack_point, int):
            self.__attack_point = attack_point
            return 0
        print("type of name is not INT")
        return 1

    def get_attack_point(self):
        """
        getteur points d'attack
        """
        return self.__attack_point

    def set_voice(self, voice="cri"):
        """
        setteur de voix
        """
        if isinstance(voice, str):
            self.__voice = voice
            return 0
        print("type of name is not STR")
        return 1

    def get_voice(self):
        """
        getteur de voix
        """
        return self.__voice

    def to_string(self):
        """
        fonction qui retourne tous les informations
        """
        return "%s a %d PV et %d PA et je dis %s" % (
            self.get_name(),
            self.get_life_point(),
            self.get_attack_point(),
            self.get_voice()
        )

    def speak(self):
        """
        fonction qui fait parler l'animal
        """
        raise NotImplementedError

    def eat(self, energy=5):
        """
        fonction pour nourrir les animaux
        """
        if isinstance(energy, int):
            self.set_life_point(self.get_life_point() + energy)

    def move(self):
        """
        fonction pour bouger les animaux
        """
        raise NotImplementedError

    def attack(self, victim):
        """
        fonction pour attacker un autre animal
        """
        victim.set_life_point(
            victim.get_life_point() - self.get_attack_point()
            )
