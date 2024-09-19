"""
animal_manager.py

Ce module contient la définition de la classe GestionElevage, qui est utilisée
pour gérer les animaux dans l'application de gestion des élevages. La classe
permet d'ajouter, de supprimer, de rechercher et d'afficher les animaux.
"""

from database import Database


class GestionElevage:
    """
    Représente un gestionnaire d'animaux dans l'élevage.

    Attributs :
        db (Database) : Instance de la classe Database pour gérer les données.
    """

    def __init__(self, db_name='animaux.db'):
        """
        Initialise une instance de GestionElevage avec une base de données.

        :param db_name: str : Le nom du fichier de la base de données.
        """
        self.db = Database(db_name)

    def ajouter_animal(self, nom, espece, date_naissance, poids):
        """
        Ajoute un nouvel animal à la base de données.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param date_naissance: str : La date de naissance de l'animal.
        :param poids: float : Le poids de l'animal en kg.
        """
        if not self.validate_string(nom) or not self.validate_string(espece):
            raise ValueError("Le nom et l'espèce doivent être valides.")

        if poids <= 0:
            raise ValueError("Le poids doit être un nombre positif.")

        self.db.ajouter_animal(nom, espece, date_naissance, poids)

    def supprimer_animal(self, nom):
        """
        Supprime un animal de la base de données par son nom.

        :param nom: str : Le nom de l'animal à supprimer.
        """
        if not self.validate_string(nom):
            raise ValueError("Le nom est nécessaire pour supprimer un animal.")

        self.db.cur.execute("DELETE FROM animaux WHERE nom = ?", (nom,))
        self.db.conn.commit()

    def afficher_animaux(self):
        """
        Affiche une chaîne décrivant tous les animaux enregistrés.

        :return: str : La chaîne décrivant les animaux.
        """
        self.db.cur.execute(
            "SELECT nom, espece, date_naissance, poids FROM animaux")
        if animaux := self.db.cur.fetchall():
            return '\n'.join(
                f"{animal[0]} ({animal[1]}), Né le {animal[2]}, "
                f"Poids: {animal[3]} kg" for animal in animaux
            )
        return "Aucun animal enregistré."

    def rechercher_animal(self, nom):
        """
        Recherche un animal par son nom.

        :param nom: str : Le nom de l'animal à rechercher.
        :return: str : La chaîne décrivant l'animal, ou un message
        si non trouvé.
        """
        if not self.validate_string(nom):
            raise ValueError(
                "Le nom est nécessaire pour rechercher un animal.")

        self.db.cur.execute(
            "SELECT nom, espece, date_naissance, poids FROM animaux "
            "WHERE nom = ?", (nom,))
        if animal := self.db.cur.fetchone():
            return (f"{animal[0]} ({animal[1]}), Né le {animal[2]}, "
                    f"Poids: {animal[3]} kg")
        return "Animal non trouvé."

    @staticmethod
    def validate_string(value):
        """
        Valide que la chaîne ne contient que des caractères alphanumériques
        et des espaces.

        :param value: str : La chaîne à valider.
        :return: bool : True si la chaîne est valide, sinon False.
        """
        return bool(value) and all(c.isalnum() or c.isspace() for c in value)
