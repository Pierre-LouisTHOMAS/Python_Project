import tkinter as tk
from tkinter import messagebox
import subprocess

class AIRENGLANDApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIRENGLAND")

        self.bandeau_height = root.winfo_screenheight() * 0.22
        self.show_dropdown = False

        self.create_menu()
        self.create_bandeau()
        self.create_buttons()  # Ajout de la création des boutons
        self.create_dropdown()

    def create_menu(self):
        self.menu = tk.Menu(self.root)

        fichier_menu = tk.Menu(self.menu, tearoff=0)
        fichier_menu.add_command(label="Enregistrer sous...", command=self.save)

        option_menu = tk.Menu(self.menu, tearoff=0)
        option_menu.add_command(label="Réglage")

        self.menu.add_cascade(label="Fichier", menu=fichier_menu)
        self.menu.add_cascade(label="Option", menu=option_menu)

        self.root.config(menu=self.menu)

    def save(self):
        print("Vous avez cliqué sur Enregistrer sous...")

    def create_bandeau(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        image_path = "../Pictures/barre_recherche.png"  # Remplacez par le chemin de votre image
        self.image_button = tk.PhotoImage(file=image_path)
        image_button_label = tk.Label(self.root, image=self.image_button, cursor="hand2")
        image_button_label.place(x=10, y=self.bandeau_height * 0.3)
        image_button_label.bind("<Button-1>", lambda e: self.toggle_dropdown())

        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.bandeau_height * 0.7, y=self.bandeau_height * 0.1)

        image_path3 = "../Pictures/Boreale.png"
        self.image3 = tk.PhotoImage(file=image_path3)
        image_label3 = tk.Label(self.root, image=self.image3)
        image_label3.place(x=0, y=self.bandeau_height * 1.05, relwidth=1, relheight=0.75)

    def create_buttons(self):
        bouton_height = int(self.bandeau_height * 0.8)

        bouton_vol = tk.Button(self.root, text="Achat Vol", width=15, command=self.redirect_to_resa_avion)
        bouton_vol.place(x=self.bandeau_height * 4.6, y=bouton_height)
        bouton_vol.bind('<Enter>', self.bouton_hover)
        bouton_vol.bind('<Leave>', self.bouton_leave)

        bouton_connexion = tk.Button(self.root, text="Connexion", width=15, command=self.redirect_to_connexion)
        bouton_connexion.place(x=self.bandeau_height * 5.4, y=bouton_height)
        bouton_connexion.bind('<Enter>', self.bouton_hover)
        bouton_connexion.bind('<Leave>', self.bouton_leave)

        bouton_creer_compte = tk.Button(self.root, text="Créer son compte", width=15)
        bouton_creer_compte.place(x=self.bandeau_height * 6.2, y=bouton_height)
        bouton_creer_compte.bind('<Enter>', self.bouton_hover)
        bouton_creer_compte.bind('<Leave>', self.bouton_leave)

    def create_dropdown(self):
        choices = ["Connexion", "Premium Economy", "Economy"]
        self.var = tk.StringVar(self.root)
        self.var.set(choices[0])
        self.option_menu = tk.OptionMenu(self.root, self.var, *choices)

    def toggle_dropdown(self):
        self.show_dropdown = not self.show_dropdown
        if self.show_dropdown:
            self.option_menu.place(x=0, y=self.bandeau_height * 0.05)
        else:
            self.option_menu.place_forget()

    def bouton_hover(self, event):
        event.widget.config(bg="lightblue")

    def bouton_leave(self, event):
        event.widget.config(bg="SystemButtonFace")

    def redirect_to_resa_avion(self):
        try:
            subprocess.Popen(["python", "resaAvionMembre.py"], shell=True)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")

    def redirect_to_connexion(self):
        try:
            subprocess.Popen(["python", "connexion.py"], shell=True)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AIRENGLANDApp(root)
    root.mainloop()
