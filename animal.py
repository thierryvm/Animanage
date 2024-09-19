"""
animal.py

Ce module contient la définition de la classe `Animal`, qui est utilisée
pour représenter un animal dans l'application de gestion des élevages.
"""


class Animal:
    """
    Représente un animal dans l'élevage.

    Attributs :
        nom (str) : Le nom de l'animal.
        espece (str) : L'espèce de l'animal.
        poids (float) : Le poids de l'animal en kg.
    """

    def __init__(self, nom, espece, poids):
        """
        Initialise une instance de Animal avec un nom, une espèce et un poids.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param poids: float : Le poids de l'animal en kg.
        """
        self.nom = nom
        self.espece = espece
        self.poids = poids

    def __str__(self):
        """
        Retourne une chaîne décrivant l'animal.

        :return: str : La chaîne décrivant l'animal.
        """
        return f"{self.nom} ({self.espece}), Poids: {self.poids} kg"
