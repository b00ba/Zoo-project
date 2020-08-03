
                                                                        ################################################
                                                                        #                                              #
                                                                        #              ZOO en OOP                      #
                                                                        #                  By                          #
                                                                        #                                              #
                                                                        #             Boubaker_Aloui                   #
                                                                        #                                              #
                                                                        #           (\(\                               #
                                                                        #           ( – -)                             #
                                                                        #           ((‘) (’)    {o,o}                  #
                                                                        #                       |)__)                  #
                                                                        #                        -""-                  #
                                                                        #                                              #
                                                                        #                                              #
                                                                        ################################################

Introduction
============

> Ce mini-projet va permettre d'apprendre le principe de classe et
> d'héritage. L'idée est de créer un Zoo en orient´e objet \`a l'aide du
> langage Python 3. Attention ce document ne contient aucune correction,
> il permet uniquement de d´efinir les sp´ecifications n´ecessaires \`a
> la cr´eation de ce mini projet. Attention les digrammes de classes ne
> sont pas complets, les getters et les setters ne sont pas pr´esents.
> De plus certaines fonctionnalit´es n´ecessitent peut ˆetre d'autre
> fonctions non affich´ees afin d'ˆetre impl´ement´ees.
>
> Les principes du zoo est le suivant:

-   Un zoo est d´efini par un nom et une liste d'enclos.

-   Un enclos est d´efini par un nom et une liste d'animaux.

-   Un animal est d´efini par un nom, des point de vies et des points
    d'attaques.

-   Il y a diff´erent type d'animaux ayant des comportements unique en
    fonction de leur type.

> Voici les diff´erentes ´ev\`enements du zoo :

-   Il peut arriver que tous les animaux d'un enclos "parlent". Chaque
    type d'animal a son propre cri.

Il est possible de nourrir tous les animaux d'un enclos, Tous les
animaux de cet enclos vont manger et gagner des points de vies.

Il peut arriver que tous les animaux d'un enclos s'attaquent
mutuellement. C'est \`a dire que chaque animal va attaquer
al´eatoirement un autre animal de l'enclos.

Tous les ´ev´enements peuvent ´egalement s'enclencher de mani\`ere
global dans tous le zoo. Dans ce cas, tous les enclos vont faire
l'´ev\`enement en mˆeme temps.

> Cela se traduit par le diagramme de classe de la figure 1.

![](media/image1.png){width="4.369061679790026in"
height="2.361561679790026in"}

> Figure 1: Le zoo

Animal
======

> Voici la classe Animal :

![](media/image2.png){width="1.61in" height="2.6099989063867017in"}

> Figure 2: Animal
>
> Cette classe est une classe abstraite permettant de d´efinir un
> animal. Ses attributs sont :

-   name : String, un nom.

-   life point : int, son nombre de point de vie.

attack point : int, son nombre de point d'attaque. d´efinit le nombre de
point de vie qu'il enl\`eve \`a un autre animal.

> Ses fonctions sont :

to string() : String, permet d'avoir une description de l'objet au
format String. exemple : "Chat1 a 10 PV et 2 PA".

-   speak(), permet d'´ecrire un "cri" dans le terminal.

-   eat(), permet de redonner 5 PV \`a l'animal.

-   move(), permet d'´ecrire un message signalant que l'animal se
    d´eplace dans le terminal.

attack(Animal), permet d'attaquer un autre animal en lui enlevant un
montant de point de vie ´egale au nombre de point d'attaque de l'animal
attaquant.

Bird et Mammal
==============

> Voici les classe Bird et Mammal :
>
> ![](media/image3.png){width="4.525in" height="3.0562489063867018in"}
>
> Figure 3: Bird et Mammal
>
> Ces classes sont des classes abstraites h´eritant de la classe Animal
> permettant de d´efinir un mammif\`ere et un oiseau.
>
> L'oiseau poss\`ede un nouvel attribut :

nb of wings : int, permet de d´efinir combien d'ailes a un oiseau. Il
doit ˆetre fix´e \`a deux par d´efaut mais devra ˆetre modifiable par
son constructeur.

> Le mammif\`ere poss\`ede un nouvel attribut :

nb of leg : int, qui permet de d´efinir combien de pattes a un
mammif\`ere. Il doit ˆetre fix´e \`a quatre par d´efaut mais devra ˆetre
modifiable par son constructeur.

> L'oiseau poss\`ede une nouvelle fonction :

fly() : String, cette fonction doit ˆetre utilis´ee par la fonction
move() afin d'avoir un texte sp´ecifique au vol.

> Le mammif\`ere poss\`ede une nouvelle fonction :

walk() : String, cette fonction doit ˆetre utilis´ee par la fonction
move() afin d'avoir un texte sp´ecifique a la marche.

> Pour les deux Classes mammif\`ere et oiseau, les fonctions suivantes
> doivent ˆetre red´efinies :

move(), permet d'´ecrire un message signalant que l'animal se d´eplace
dans le terminal. L'oiseau doit utiliser fly() et le mammif\`ere doit
utiliser walk().

to string(): String, permet d'avoir une description de l'objet au format
String. Cependant, il faut ajouter le nombre d'aile pour l'oiseau et le
nombre de patte pour les mammif\`eres dans cette description.

Eagle, Pigeon, Tiger, Person, Cat et Dog
========================================

> Voici les classes Eagle, Pigeon, Tiger, Person, Cat et Dog :
>
> ![](media/image4.png){width="6.397083333333334in"
> height="2.090832239720035in"}
>
> Figure 4: Eagle, Pigeon, Tiger, Person, Cat et Dog
>
> Les classes Eagle et Pigeon h´erite de la classe Bird. Les classes
> Tiger, Person, Cat et Dog h´eritent de la classes Mammal. Toutes les
> classes doivent red´efinir la fonction :

-   speak(), afin de d´efinir un message diff´erent pour chaque classe.

> La classe Person poss\`ede un nouvel attribut :

-   first name : String

> La classe doit red´efinir la fonction :

-   to string() : String, afin d'ajouter l'attribut first name \`a la
    description.

Enclosure
=========

> Voici la classe Enclosure :

![](media/image5.png){width="1.3416655730533684in"
height="2.091666666666667in"}

> Figure 5: Enclosure La classe Enclosure, d´efinit un enclos. Ses
> attributs sont :

-   name : String, un nom.

-   list animal : list(Animal), une liste d'animaux que contient
    l'enclos.

> Ses fonctions sont :

to string() : String, permet d'avoir une description de l'objet au
format String. Exemple : "L'enclos appel´e prison1 contient :

-   Chat1 a 10 PV et 2 PA qui a 4 pattes

-   Aigle1 a 10 PV et 2 PA qui a 2 ailes"

```{=html}
<!-- -->
```
-   feed all(), permet de nourrir tous les animaux de la liste.

-   add animal(Animal), permet d'ajouter un Animal dans la liste.

-   remove animal(pos), permet de retirer un Animal de la liste en
    fonction de sa position dans la liste.

-   all speaking(), permet de faire parler tous les animaux de l'enclos.

all attacking(), permet de faire attaquer tous les animaux un \`a un. Un
animal va attaquer al´eatoirement un autre animal de l'enclos. Si, un
animal est \`a 0 PV ou moins il doit ˆetre retir´e de la liste.

Zoo
===

> Voici la classe Zoo:

![](media/image6.png){width="1.3416666666666666in"
height="1.808332239720035in"}

> Figure 6: Zoo La classe Zoo d´efinit un zoo. Ses attributs sont :

-   name : String, un nom.

-   list enclosure : list(Enclosure), une liste d'enclos que contient le
    zoo.

> Ses fonctions sont :

to string() : String, permet d'avoir une description de l'objet au
format String. Exemple : "Le zoo appel´e Zoomba contient :

L'enclos appel´e prison1 contient :

-   Chat1 a 10 PV et 2 PA qui a 4 pattes

-   Aigle1 a 10 PV et 2 PA qui a 2 ailes L'enclos appel´e prison2
    contient :

-   Chat2 a 10 PV et 2 PA qui a 4 pattes

-   Aigle2 a 10 PV et 2 PA qui a 2 ailes"

    -   feed all(), permet de donner de la nourriture dans tous les
        enclos de la liste.

create enclosure(name) : Enclosure, permet de cr´eer un enclos avec le
nom name, de l'ajouter dans la liste d'enclos et de le retourner. Si le
nom est d´ej\`a pris par un autre enclos alors la fonction retourne
None.

-   all speaking() : permet de faire parler tous les animaux de tous les
    enclos.

-   all attacking(), permet de faire attaquer tous les animaux de tous
    les enclos.

Exercice
========

> Afin de faire cette exercice, il est important de faire les questions
> dans l'ordre. De plus, il vous est demand´e de r´ealiser ce projet sur
> GitLab. Il est ´egalement obligatoire de respecter la Pep8 via pylint
> et de faire des tests unitaires via pytest pour chaque question.

1.  Animal
    ------

    1.  R´ealisez la classe Animal.

    2.  R´edigez un main.py dans le quelle vous instanciez deux Animal.
        Utilisez les fonctions to string(), speak(), eat() et move()
        d'un Animal puis attack() avec l'autre Animal. V´erifiez bien
        les PV des animaux.

    3.  N'oubliez pas de r´ediger les tests unitaires et de respecter la
        Pep8.

    4.  Faites un premier tag sur git avec la version V1.00.

2.  Bird et Mammal
    --------------

    1.  R´ealisez les Classes Bird et Mammal (conseil : pour la fonction
        to string(), vous pouvez utiliser la fonc- tion to string de la
        classe Animal dans votre fonction et la compl´eter des
        informations suppl´ementaires)

    2.  Modifiez la fonction move() de la classe Animal afin quelle
        soul\`eve une erreur si la fonction move() n'est pas
        impl´ement´e dans ces sous-classes (big help :
        NotImplementedError("Subclasses should implement this!")

    3.  Modifiez votre main.py dans le quelle vous instanciez un Animal,
        un Bird et un Mammal. Testez les diff´erentes fonctions.
        V´erifiez que l'Animal retourne bien une exception quand la
        fonction move() est utilis´e (help : try \... except \...).

    4.  N'oubliez pas de r´ediger/modifier les tests unitaires et de
        respecter la Pep8.

    5.  Faites un second tag sur git avec la version V2.00.

3.  Eagle, Pigeon, Tiger, Person, Cat et Dog
    ----------------------------------------

    1.  R´ealisez les classes Eagle, Pigeon, Tiger, Person, Cat et Dog
        (conseil : pour la fonction to string() de Person, vous pouvez
        utiliser la fonction to string de la classe Mammal dans votre
        fonction et la compl´eter des informations suppl´ementaire)

    2.  Modifier la fonction speak() de la classe Animal afin quelle
        retourne une erreur si la fonction n'est pas impl´ement´e dans
        ces sous-classes.

    3.  Modifiez votre main.py dans le quelle vous instanciez un objet
        de chaque classes. Testez les diff´erentes fonctions. V´erifiez
        que l'Animal retourne bien une exception quand la fonction
        move() ou speak() est utilis´e (help : try \... except \...).
        V´erifiez bien que Eagle, Pigeon, Tiger, Person, Cat et Dog ont
        bien un crie diff´erent via la fonction speak()

    4.  N'oubliez pas de r´ediger/modifier les tests unitaires et de
        respecter la Pep8.

    5.  Faites un troisi\`eme tag sur git avec la version V3.00.

4.  Enclosure
    ---------

    1.  R´ealisez la Classe Enclosure (conseil : pour la fonction to
        string() n'h´esitez pas \`a utiliser la fonction to string() des
        Animaux de votre liste)

    2.  Utilisez le module random pour la fonction all attacking() pour
        s'assurer du choix al´eatoire.

    3.  Modifiez votre main.py. Instanciez un Enclosure et des animaux
        de diff´erentes classes. Testez votre enclos et v´erifiez
        l'´etat de celui-ci avant et apr\`es all attacking()

    4.  N'oubliez pas de r´ediger/modifier les tests unitaires et de
        respecter la Pep8.

    5.  Faites un quatri\`eme tag sur git avec la version V4.00.

5.  Zoo
    ---

    1.  R´ealisez la Classe Zoo (conseil : pour la fonction to string()
        n'h´esitez pas \`a utiliser la fonction to string() des
        Enclosure de votre liste)

    2.  Modifiez votre main.py. Instanciez un Zoo, des enclos et des
        animaux de diff´erentes classes. Testez votre zoo et v´erifiez
        l'´etat de celui-ci avant et apr\`es all attacking()

    3.  N'oubliez pas de r´ediger/modifier les tests unitaires et de
        respecter la Pep8.

    4.  Faites un cinqui\`eme tag sur git avec la version V5.00.
