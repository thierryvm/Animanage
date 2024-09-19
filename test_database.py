"""
test_database.py

Ce module contient des tests unitaires pour la classe `Database` qui gère
les interactions avec la base de données SQLite.
"""

import unittest
import os
from database import Database


class TestDatabase(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe Database.
    """

    def setUp(self):
        """
        Initialise une instance de Database avant chaque test.
        Crée une base de données de test.
        """
        self.db_name = 'test_animaux.db'
        self.db = Database(self.db_name)

    def tearDown(self):
        """
        Ferme la connexion à la base de données et supprime le fichier
        de la base de données après chaque test.
        """
        self.db.fermer_connexion()
        os.remove(self.db_name)

    def test_ajouter_animal(self):
        """
        Teste l'ajout d'un animal dans la base de données.
        """
        self.db.ajouter_animal('Rex', 'Chien', '2020-01-01', 10.5)
        self.db.cur.execute("SELECT * FROM animaux WHERE nom = 'Rex'")
        animal = self.db.cur.fetchone()
        self.assertIsNotNone(animal)
        self.assertEqual(animal[1], 'Rex')


if __name__ == '__main__':
    unittest.main()
