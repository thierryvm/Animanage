"""
animal_manager.py

Ce module contient la définition de la classe GestionElevage, qui est utilisée
pour gérer les animaux dans l'application de gestion des élevages. La classe
permet d'ajouter, de supprimer, de rechercher et d'afficher les animaux.
"""


class GestionElevage:
    """
    Représente un gestionnaire d'animaux dans l'élevage.

    Attributs :
        animaux (list) : Liste des animaux enregistrés.
    """

    def __init__(self):
        """
        Initialise une instance de GestionElevage avec une liste vide
        d'animaux.
        """
        self.animaux = []

    def ajouter_animal(self, nom, espece, poids):
        """
        Ajoute un nouvel animal à la liste des animaux.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param poids: float : Le poids de l'animal en kg.
        """
        if not self.validate_string(nom) or not self.validate_string(espece):
            raise ValueError("Le nom et l'espèce doivent être valides.")

        if poids <= 0:
            raise ValueError("Le poids doit être un nombre positif.")

        animal = {
            'nom': nom,
            'espece': espece,
            'poids': poids
        }
        self.animaux.append(animal)

    def supprimer_animal(self, nom):
        """
        Supprime un animal de la liste des animaux par son nom.

        :param nom: str : Le nom de l'animal à supprimer.
        """
        if not self.validate_string(nom):
            raise ValueError("Le nom est nécessaire pour supprimer un animal.")

        self.animaux = [
            animal for animal in self.animaux if animal['nom'] != nom
        ]

    def afficher_animaux(self):
        """
        Affiche une chaîne décrivant tous les animaux enregistrés.

        :return: str : La chaîne décrivant les animaux.
        """
        if not self.animaux:
            return "Aucun animal enregistré."
        return '\n'.join(
            f"{animal['nom']} ({animal['espece']}), "
            f"Poids: {animal['poids']} kg"
            for animal in self.animaux
        )

    def rechercher_animal(self, nom):
        """
        Recherche un animal par son nom.

        :param nom: str : Le nom de l'animal à rechercher.
        :return: str : La chaîne décrivant l'animal, ou un message si
                        non trouvé.
        """
        if not self.validate_string(nom):
            raise ValueError("Le nom est nécessaire pour rechercher"
                             "un animal.")

        return next(
            (
                f"{animal['nom']} ({animal['espece']}), "
                f"Poids: {animal['poids']} kg"
                for animal in self.animaux
                if animal['nom'] == nom
            ),
            "Animal non trouvé."
        )

    @staticmethod
    def validate_string(value):
        """
        Valide que la chaîne ne contient que des caractères alphanumériques
        et des espaces.

        :param value: str : La chaîne à valider.
        :return: bool : True si la chaîne est valide, sinon False.
        """
        return bool(value) and all(c.isalnum() or c.isspace() for c in value)
