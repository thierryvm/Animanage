"""
Création de l'application Animanage.
"""

import tkinter as tk
from tkinter import simpledialog, messagebox
from animal_manager import GestionElevage


class Application:
    """
    Représente l'application GUI pour la gestion des animaux.
    """

    def __init__(self, main_window):
        """
        Initialise l'application avec une fenêtre principale.
        """
        self.gestion = GestionElevage()
        self.main_window = main_window
        main_window.title("Gestion d'Élevage")

        # Configure les éléments de l'interface
        self.label = tk.Label(
            main_window,
            text="Gestion d'Élevage",
            font=('Helvetica', 16)
        )
        self.label.pack(pady=10)

        self.add_button = tk.Button(
            main_window,
            text="Ajouter Animal",
            command=self.add_animal
        )
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            main_window,
            text="Supprimer Animal",
            command=self.delete_animal
        )
        self.delete_button.pack(pady=5)

        self.show_button = tk.Button(
            main_window,
            text="Afficher Animaux",
            command=self.show_animals
        )
        self.show_button.pack(pady=5)

    def add_animal(self):
        """
        Ajoute un animal à l'élevage en demandant des informations
        à l'utilisateur.
        """
        nom = simpledialog.askstring("Nom", "Entrez le nom de l'animal:")
        espece = simpledialog.askstring(
            "Espèce", "Entrez l'espèce de l'animal:"
        )
        poids = simpledialog.askfloat(
            "Poids", "Entrez le poids de l'animal en kg:"
        )

        # Validation stricte des entrées
        if not self.validate_name(nom):
            messagebox.showwarning(
                "Erreur", "Le nom doit contenir uniquement des lettres "
                "et des espaces."
            )
            return

        if not self.validate_name(espece):
            messagebox.showwarning(
                "Erreur", "L'espèce doit contenir uniquement des lettres "
                "et des espaces."
            )
            return

        if poids is None or poids <= 0:
            messagebox.showwarning(
                "Erreur", "Le poids doit être un nombre positif."
            )
            return

        self.gestion.ajouter_animal(nom, espece, poids)
        messagebox.showinfo("Succès", f"Animal {nom} ajouté.")

    def delete_animal(self):
        """
        Supprime un animal de l'élevage en demandant le nom à l'utilisateur.
        """
        nom = simpledialog.askstring(
            "Nom", "Entrez le nom de l'animal à supprimer:"
        )

        if not self.validate_name(nom):
            messagebox.showwarning(
                "Erreur", "Le nom est nécessaire pour supprimer un animal "
                "et doit être valide."
            )
            return

        self.gestion.supprimer_animal(nom)
        messagebox.showinfo("Succès", f"Animal {nom} supprimé.")

    def show_animals(self):
        """
        Affiche la liste des animaux dans une boîte de dialogue.
        """
        animaux = self.gestion.afficher_animaux()
        messagebox.showinfo("Animaux", animaux)

    @staticmethod
    def validate_name(value):
        """
        Valide que la chaîne ne contient que des caractères alphabétiques et
        des espaces.

        :param value: str : La chaîne à valider.
        :return: bool : True si la chaîne est valide, sinon False.
        """
        return bool(value) and all(
            c.isalpha() or c.isspace() for c in value
        )


if __name__ == "__main__":
    root_window = tk.Tk()  # Renommé pour éviter le conflit avec main_window
    app = Application(root_window)
    root_window.mainloop()
