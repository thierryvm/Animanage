"""
animal.py

Ce module contient la définition de la classe `Animal`, qui est utilisée pour
représenter un animal dans l'application de gestion des élevages. La classe
permet de stocker et d'afficher les informations relatives à un animal.
"""


class Animal:
    """
    Représente un animal.

    Attributs :
        nom (str) : Le nom de l'animal.
        espece (str) : L'espèce de l'animal.
        poids (float) : Le poids de l'animal en kg.
    """

    def __init__(self, nom, espece, poids):
        """
        Initialise un nouvel animal.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param poids: float : Le poids de l'animal en kg.
        """
        self.nom = nom
        self.espece = espece
        self.poids = poids

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères
        des détails de l'animal.
        """
        return f"{self.nom} ({self.espece}), Poids: {self.poids} kg"
