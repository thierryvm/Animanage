"""
test_animal_manager.py
"""

import unittest
from animal_manager import GestionElevage


class TestGestionElevage(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe GestionElevage.
    """

    def setUp(self):
        """
        Initialise une instance de GestionElevage avant chaque test.
        """
        self.gestion_elevage = GestionElevage()

    def test_ajouter_animal(self):
        """
        Teste l'ajout d'un animal.
        """
        self.gestion_elevage.ajouter_animal('Rex', 'Chien', 10.5)
        self.assertEqual(len(self.gestion_elevage.animaux), 1)
        self.assertEqual(self.gestion_elevage.animaux[0]['nom'], 'Rex')

    def test_supprimer_animal(self):
        """
        Teste la suppression d'un animal.
        """
        self.gestion_elevage.ajouter_animal('Rex', 'Chien', 10.5)
        self.gestion_elevage.supprimer_animal('Rex')
        self.assertEqual(len(self.gestion_elevage.animaux), 0)

    def test_afficher_animaux(self):
        """
        Teste l'affichage des animaux.
        """
        self.gestion_elevage.ajouter_animal('Rex', 'Chien', 10.5)
        self.gestion_elevage.ajouter_animal('Mia', 'Chat', 3.2)
        affichage = self.gestion_elevage.afficher_animaux()
        self.assertIn('Rex (Chien), Poids: 10.5 kg', affichage)
        self.assertIn('Mia (Chat), Poids: 3.2 kg', affichage)

    def test_rechercher_animal(self):
        """
        Teste la recherche d'un animal.
        """
        self.gestion_elevage.ajouter_animal('Rex', 'Chien', 10.5)
        resultat = self.gestion_elevage.rechercher_animal('Rex')
        self.assertEqual(resultat, 'Rex (Chien), Poids: 10.5 kg')

    def test_rechercher_animal_non_existant(self):
        """
        Teste la recherche d'un animal qui n'existe pas.
        """
        resultat = self.gestion_elevage.rechercher_animal('Inconnu')
        self.assertEqual(resultat, 'Animal non trouvé.')


if __name__ == '__main__':
    unittest.main()
