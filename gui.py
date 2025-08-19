import tkinter as tk
from tkinter import ttk
from calculator import FiberLossCalculator
from plotter import plot_fiber_losses


class FiberOpticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur de Pertes Fibre Optique")
        self.root.geometry("900x600")

        # Variables
        self.fiber_length = tk.DoubleVar(value=1.0)
        self.alpha_db = tk.DoubleVar(value=0.2)
        self.connector_loss = tk.DoubleVar(value=0.5)
        self.splice_loss = tk.DoubleVar(value=0.1)
        self.num_connectors = tk.IntVar(value=2)
        self.num_splices = tk.IntVar(value=1)

        # Frame principale
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill="both", expand=True)

        # Formulaire de saisie
        self._create_input_form()

        # Bouton de calcul
        ttk.Button(
            self.main_frame,
            text="Calculer les Pertes",
            command=self.calculate_and_plot
        ).pack(pady=10)

        # Zone de résultat
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill="both", expand=True)

    def _create_input_form(self):
        form_frame = ttk.LabelFrame(self.main_frame, text="Paramètres de la Fibre", padding="10")
        form_frame.pack(fill="x", pady=5)

        ttk.Label(form_frame, text="Longueur (km):").grid(row=0, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.fiber_length).grid(row=0, column=1, sticky="ew")

        ttk.Label(form_frame, text="Atténuation (dB/km):").grid(row=1, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.alpha_db).grid(row=1, column=1, sticky="ew")

        ttk.Label(form_frame, text="Perte par connecteur (dB):").grid(row=2, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.connector_loss).grid(row=2, column=1, sticky="ew")

        ttk.Label(form_frame, text="Nombre de connecteurs:").grid(row=3, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.num_connectors).grid(row=3, column=1, sticky="ew")

        ttk.Label(form_frame, text="Perte par épissure (dB):").grid(row=4, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.splice_loss).grid(row=4, column=1, sticky="ew")

        ttk.Label(form_frame, text="Nombre d'épissures:").grid(row=5, column=0, sticky="w")
        ttk.Entry(form_frame, textvariable=self.num_splices).grid(row=5, column=1, sticky="ew")

        form_frame.columnconfigure(1, weight=1)

    def calculate_and_plot(self):
        calculator = FiberLossCalculator(
            fiber_length_km=self.fiber_length.get(),
            alpha_db_km=self.alpha_db.get(),
            connector_loss_db=self.connector_loss.get(),
            splice_loss_db=self.splice_loss.get(),
            num_connectors=self.num_connectors.get(),
            num_splices=self.num_splices.get()
        )

        # Efface l'ancien graphique
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Affiche le nouveau graphique
        plot_fiber_losses(calculator, self.result_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = FiberOpticsGUI(root)
    root.mainloop()