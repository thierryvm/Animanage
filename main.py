"""
Création de l'application Animanage.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from animal_manager import GestionElevage
from calendrier import Calendrier


class Application:
    """
    Représente l'application GUI pour la gestion des animaux.
    """

    def __init__(self, main_window):
        """
        Initialise l'application avec une fenêtre principale.
        """
        self.gestion = GestionElevage()
        self.calendrier = Calendrier()
        self.main_window = main_window
        main_window.title("Animanage")
        main_window.geometry("1000x600")
        main_window.configure(bg="#F0F0F0")

        self.setup_ui()

    def setup_ui(self):
        """Configure l'interface utilisateur."""
        # Barre latérale
        sidebar = tk.Frame(self.main_window, bg="#2C3E50", width=200)
        sidebar.pack(side="left", fill="y")

        # Logo (remplacez par votre propre logo)
        logo_label = tk.Label(sidebar, text="Animanage", font=(
            "Helvetica", 20, "bold"), bg="#2C3E50", fg="white")
        logo_label.pack(pady=20)

        # Boutons de la barre latérale
        buttons = [
            ("Tableau de bord", self.show_dashboard),
            ("Ajouter Animal", self.add_animal),
            ("Afficher Animaux", self.show_animals),
            ("Ajouter Événement", self.add_event),
            ("Afficher Événements", self.show_events),
        ]

        for text, command in buttons:
            btn = tk.Button(sidebar, text=text, command=command, bg="#34495E",
                            fg="white",
                            font=("Helvetica", 12), bd=0, padx=10, pady=5)
            btn.pack(fill="x", padx=10, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#4E5F70"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#34495E"))

        # Zone principale
        main_area = tk.Frame(self.main_window, bg="#ECF0F1")
        main_area.pack(side="right", fill="both", expand=True)

        # Titre de la zone principale
        self.main_title = tk.Label(main_area, text="Tableau de bord", font=(
            "Helvetica", 24, "bold"), bg="#ECF0F1")
        self.main_title.pack(pady=20)

        # Contenu de la zone principale (à remplir dynamiquement)
        self.content_frame = tk.Frame(main_area, bg="#ECF0F1")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def show_dashboard(self):
        """Affiche le tableau de bord."""
        self.clear_content()
        self.main_title.config(text="Tableau de bord")
        # Ajoutez ici le contenu du tableau de bord

    def add_animal(self):
        """Ajoute un animal à l'élevage."""
        self.clear_content()
        self.main_title.config(text="Ajouter un animal")

        frame = ttk.Frame(self.content_frame)
        frame.pack(padx=20, pady=20)

        ttk.Label(frame, text="Nom:").grid(
            row=0, column=0, sticky="e", padx=5, pady=5)
        nom_entry = ttk.Entry(frame)
        nom_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Espèce:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5)
        espece_entry = ttk.Entry(frame)
        espece_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Date de naissance:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5)
        date_entry = ttk.Entry(frame)
        date_entry.grid(row=2, column=1, padx=5, pady=5)
        date_entry.insert(0, "JJ-MM-AAAA")

        ttk.Label(frame, text="Poids (kg):").grid(
            row=3, column=0, sticky="e", padx=5, pady=5)
        poids_entry = ttk.Entry(frame)
        poids_entry.grid(row=3, column=1, padx=5, pady=5)

        def save_animal():
            nom = nom_entry.get()
            espece = espece_entry.get()
            date_naissance = date_entry.get()
            poids = poids_entry.get()

            try:
                poids = float(poids)
                datetime.strptime(date_naissance, '%d-%m-%Y')
            except ValueError:
                messagebox.showerror(
                    "Erreur", "Format de date ou de poids invalide.")
                return

            self.gestion.ajouter_animal(nom, espece, date_naissance, poids)
            messagebox.showinfo("Succès", f"Animal {nom} ajouté.")
            self.show_dashboard()

        ttk.Button(frame, text="Enregistrer", command=save_animal).grid(
            row=4, column=0, columnspan=2, pady=10)

    def show_animals(self):
        """Affiche la liste des animaux."""
        self.clear_content()
        self.main_title.config(text="Liste des animaux")

        animals = self.gestion.afficher_animaux().split('\n')
        for animal in animals:
            ttk.Label(self.content_frame, text=animal).pack(pady=2)

    def add_event(self):
        """Ajoute un événement au calendrier."""
        self.clear_content()
        self.main_title.config(text="Ajouter un événement")

        frame = ttk.Frame(self.content_frame)
        frame.pack(padx=20, pady=20)

        ttk.Label(frame, text="Titre:").grid(
            row=0, column=0, sticky="e", padx=5, pady=5)
        titre_entry = ttk.Entry(frame)
        titre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Description:").grid(
            row=1, column=0, sticky="e", padx=5, pady=5)
        description_entry = ttk.Entry(frame)
        description_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Date:").grid(
            row=2, column=0, sticky="e", padx=5, pady=5)
        date_entry = ttk.Entry(frame)
        date_entry.grid(row=2, column=1, padx=5, pady=5)
        date_entry.insert(0, "JJ-MM-AAAA")

        ttk.Label(frame, text="Heure:").grid(
            row=3, column=0, sticky="e", padx=5, pady=5)
        heure_entry = ttk.Entry(frame)
        heure_entry.grid(row=3, column=1, padx=5, pady=5)
        heure_entry.insert(0, "HH:MM")

        def save_event():
            titre = titre_entry.get()
            description = description_entry.get()
            date_str = f"{date_entry.get()} {heure_entry.get()}"
            try:
                datetime.strptime(date_str, '%d-%m-%Y %H:%M')
            except ValueError:
                messagebox.showerror(
                    "Erreur", "Format de date ou d'heure invalide.")
                return

            self.calendrier.ajouter_evenement(titre, description, date_str)
            messagebox.showinfo("Succès", f"Événement {titre} ajouté.")
            self.show_dashboard()

        ttk.Button(frame, text="Enregistrer", command=save_event).grid(
            row=4, column=0, columnspan=2, pady=10)

    def show_events(self):
        """Affiche la liste des événements."""
        self.clear_content()
        self.main_title.config(text="Liste des événements")

        events = self.calendrier.afficher_evenements().split('\n')
        for event in events:
            ttk.Label(self.content_frame, text=event).pack(pady=2)

    def clear_content(self):
        """Efface le contenu de la zone principale."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root_window = tk.Tk()
    app = Application(root_window)
    root_window.mainloop()
