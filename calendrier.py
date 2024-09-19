"""
calendrier.py

Ce module contient la définition de la classe `Calendrier`, qui est utilisée
pour gérer les rendez-vous et les événements dans l'application de gestion
des élevages.
"""

from datetime import datetime
import sqlite3


class Evenement:
    """
    Représente un événement dans le calendrier.

    Attributs :
        titre (str) : Le titre de l'événement.
        description (str) : La description de l'événement.
        date (datetime) : La date et l'heure de l'événement.
    """

    def __init__(self, titre, description, date):
        """
        Initialise une instance de Evenement avec un titre, une description et
        une date.

        :param titre: str : Le titre de l'événement.
        :param description: str : La description de l'événement.
        :param date: datetime : La date et l'heure de l'événement.
        """
        self.titre = titre
        self.description = description
        self.date = date

    def __str__(self):
        """
        Retourne une chaîne décrivant l'événement.

        :return: str : La chaîne décrivant l'événement.
        """
        return (f"{self.titre} - {self.description} le "
                f"{self.date.strftime('%d-%m-%Y %H:%M')}")


class Calendrier:
    """
    Représente un calendrier pour gérer les événements.

    Attributs :
        db (sqlite3.Connection) : Connexion à la base de données.
        cur (sqlite3.Cursor) : Curseur pour exécuter des commandes SQL.
    """

    def __init__(self, db_name='evenements.db'):
        """
        Initialise une instance de Calendrier avec une base de données.

        :param db_name: str : Le nom du fichier de la base de données.
        """
        self.db = sqlite3.connect(db_name)
        self.cur = self.db.cursor()
        self.creer_table_evenements()

    def creer_table_evenements(self):
        """
        Crée la table des événements si elle n'existe pas déjà.
        """
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS evenements (
                id INTEGER PRIMARY KEY,
                titre TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.db.commit()

    def ajouter_evenement(self, titre, description, date_str):
        """
        Ajoute un nouvel événement au calendrier.

        :param titre: str : Le titre de l'événement.
        :param description: str : La description de l'événement.
        :param date_str: str : La date et l'heure de l'événement sous forme
        de chaîne.
        """
        # Convertir la chaîne de date en objet datetime
        date = datetime.strptime(date_str, '%d-%m-%Y %H:%M')

        # Insérer l'événement dans la base de données
        self.cur.execute('''
            INSERT INTO evenements (titre, description, date)
            VALUES (?, ?, ?)
        ''', (titre, description, date.strftime('%d-%m-%Y %H:%M')))
        self.db.commit()

    def supprimer_evenement(self, titre):
        """
        Supprime un événement du calendrier par son titre.

        :param titre: str : Le titre de l'événement à supprimer.
        """
        self.cur.execute("DELETE FROM evenements WHERE titre = ?", (titre,))
        self.db.commit()

    def afficher_evenements(self):
        """
        Affiche une chaîne décrivant tous les événements enregistrés.

        :return: str : La chaîne décrivant les événements.
        """
        self.cur.execute("SELECT titre, description, date FROM evenements")
        if evenements := self.cur.fetchall():
            return '\n'.join(
                f"{evenement[0]} - {evenement[1]} le {evenement[2]}"
                for evenement in evenements
            )
        else:
            return "Aucun événement enregistré."

    def rechercher_evenement(self, titre):
        """
        Recherche un événement par son titre.

        :param titre: str : Le titre de l'événement à rechercher.
        :return: str : La chaîne décrivant l'événement, ou un message si
        non trouvé.
        """
        self.cur.execute(
            "SELECT titre, description, date FROM evenements WHERE titre = ?",
            (titre,)
        )
        if evenement := self.cur.fetchone():
            return f"{evenement[0]} - {evenement[1]} le {evenement[2]}"
        return "Événement non trouvé."
