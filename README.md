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

description:
============
Un mini projet sur lequel je le prépare au même temps que mon sujet de stage afin d`approfondir mes connaissances en langage Python 3. Ce projet permet d apprendre le principe de classe et d héritage voire aussi le travail sur Gitlab afin de lancer les tests et la vérification de la qualité de code a chaque Push de façon régulière et indépendamment de l espace de travail.
(voir zoo.pdf)

techniques utilisées:
============
Python 3, PEP 8, PIP, Gitlab, Virtual-env

Installation basique:
============
Cette installation comprend l'installation du projet de base sans la prise en compte de l'installation du shield GrovePi+. Cette installation est possible sur n'importe quelle machine mais ne permettra pas d'utiliser les capteurs Grove.

Pour utiliser ce projet, il faut installer les packages suivant :
* git
* python3-dev
* python3-venv

Voici les différentes étapes à suivre pour installer le projet :
1. Cloner le git : `git clone git@github.com:b00ba/Zoo-project.git`
2. Entrer dans le fichier adi3d : `cd Zoo-project`
3. Créer un virtual env python3 : `python -m venv venv`
4. Installer les librairies nécessaire pour le projet : `pip install -r requirements.txt`

Il est à noter que pour ce projet utilise la version 3.6.7 de Python.

Dépendance:
============
Les dépendances sont installées automatiquement lors de l’exécution de la commande : `pip install -r requirements.txt` 
dans le virtual env.
