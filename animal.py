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
        date_naissance (str) : La date de naissance de l'animal
                                (format AAAA-MM-JJ).
        poids (float) : Le poids de l'animal en kg.
    """

    def __init__(self, nom, espece, date_naissance, poids):
        """
        Initialise un nouvel animal.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param date_naissance: str : La date de naissance de l'animal
                                    (format AAAA-MM-JJ).
        :param poids: float : Le poids de l'animal en kg.
        """
        self.nom = nom
        self.espece = espece
        self.date_naissance = date_naissance
        self.poids = poids

    def afficher_details(self):
        """
        Affiche les détails de l'animal.
        """
        print(f"Nom : {self.nom}")
        print(f"Espèce : {self.espece}")
        print(f"Date de naissance : {self.date_naissance}")
        print(f"Poids : {self.poids} kg")
