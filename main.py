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
            main_window, text="Gestion d'Élevage", font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(
            main_window, text="Ajouter Animal", command=self.add_animal)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(
            main_window, text="Supprimer Animal", command=self.delete_animal)
        self.delete_button.pack(pady=5)

        self.show_button = tk.Button(
            main_window, text="Afficher Animaux", command=self.show_animals)
        self.show_button.pack(pady=5)

    def add_animal(self):
        """
        Ajoute un animal à l'élevage en demandant des informations
        à l'utilisateur.
        """
        nom = simpledialog.askstring("Nom", "Entrez le nom de l'animal:")
        espece = simpledialog.askstring(
            "Espèce", "Entrez l'espèce de l'animal:")
        poids = simpledialog.askfloat(
            "Poids", "Entrez le poids de l'animal en kg:")
        if nom and espece and poids is not None:
            self.gestion.ajouter_animal(nom, espece, poids)
            messagebox.showinfo("Succès", f"Animal {nom} ajouté.")
        else:
            messagebox.showwarning(
                "Erreur", "Tous les champs sont nécessaires.")

    def delete_animal(self):
        """
        Supprime un animal de l'élevage en demandant le nom à l'utilisateur.
        """
        if nom := simpledialog.askstring(
            "Nom", "Entrez le nom de l'animal à supprimer:"
        ):
            self.gestion.supprimer_animal(nom)
            messagebox.showinfo("Succès", f"Animal {nom} supprimé.")
        else:
            messagebox.showwarning("Erreur", "Le nom est nécessaire"
                                   "pour supprimer un animal.")

    def show_animals(self):
        """
        Affiche la liste des animaux dans une boîte de dialogue.
        """
        animaux = self.gestion.afficher_animaux()
        messagebox.showinfo("Animaux", animaux)


if __name__ == "__main__":
    main_windows = tk.Tk()
    app = Application(main_windows)
    main_windows.mainloop()
