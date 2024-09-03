"""
database.py

Ce module fournit des fonctionnalités pour interagir avec une base de
données SQLite.
Il contient la classe `Database` pour gérer la création de tables,
l'ajout d'animaux
et la gestion des connexions à la base de données.
"""

import sqlite3


class Database:
    """
    Représente une connexion à une base de données SQLite pour la gestion
    des animaux.

    Attributs :
        conn (sqlite3.Connection) : La connexion à la base de données.
        cur (sqlite3.Cursor) : Le curseur pour exécuter des commandes SQL.
    """

    def __init__(self, db_name):
        """
        Initialise une connexion à la base de données SQLite et crée
        les tables nécessaires.

        :param db_name: str : Le nom du fichier de la base de données.
        """
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.creer_table_animaux()

    def creer_table_animaux(self):
        """
        Crée la table des animaux si elle n'existe pas déjà.
        """
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS animaux (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                espece TEXT NOT NULL,
                date_naissance TEXT NOT NULL,
                poids REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def ajouter_animal(self, nom, espece, date_naissance, poids):
        """
        Ajoute un nouvel animal à la base de données.

        :param nom: str : Le nom de l'animal.
        :param espece: str : L'espèce de l'animal.
        :param date_naissance: str : La date de naissance de l'animal
                                    (format AAAA-MM-JJ).
        :param poids: float : Le poids de l'animal en kg.
        """
        if not self.validate_string(nom) or not self.validate_string(espece):
            raise ValueError("Le nom et l'espèce doivent être valides.")

        if poids <= 0:
            raise ValueError("Le poids doit être un nombre positif.")

        self.cur.execute('''
            INSERT INTO animaux (nom, espece, date_naissance, poids)
            VALUES (?, ?, ?, ?)
        ''', (nom, espece, date_naissance, poids))
        self.conn.commit()

    def fermer_connexion(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

    @staticmethod
    def validate_string(value):
        """
        Valide que la chaîne ne contient que des caractères alphanumériques
        et des espaces.

        :param value: str : La chaîne à valider.
        :return: bool : True si la chaîne est valide, sinon False.
        """
        return bool(value) and all(c.isalnum() or c.isspace() for c in value)
