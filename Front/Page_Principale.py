import tkinter as tk
from tkinter import messagebox
import subprocess

# Création de la fenêtre principale
root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("AIRENGLAND")

# Hauteur du bandeau
bandeau_height = root.winfo_screenheight() * 0.22

# Variable pour gérer l'affichage de la liste déroulante
show_dropdown = False

# Fonction pour afficher/masquer la liste déroulante
def toggle_dropdown():
    global show_dropdown
    show_dropdown = not show_dropdown
    if show_dropdown:
        option_menu.place(x=0, y=bandeau_height * 0.05)
    else:
        option_menu.place_forget()

# Bandeau en fond blanc
canvas = tk.Canvas(root, bg="white")
canvas.place(x=0, y=0, relwidth=1, relheight=0.20)  # Bandeau sur 20% de la hauteur


image_path = "../Pictures/barre_recherche.png"
image_button = tk.PhotoImage(file=image_path)
#image_button = image_button.subsample(2)
image_button_label = tk.Label(root, image=image_button, cursor="hand2")
image_button_label.place(x=10, y=bandeau_height * 0.3)
image_button_label.bind("<Button-1>", lambda e: toggle_dropdown())

# Ajouter une liste déroulante initialement masquée
choices = ["Connexion", "Premium Economy", "Economy"]
var = tk.StringVar(root)
var.set(choices[0])
option_menu = tk.OptionMenu(root, var, *choices)


image_path = "../Pictures/Boreale.png"
image = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=image)
image_label.place(x=0, y=bandeau_height * 1.05, relwidth=1, relheight=0.75)

def bouton_hover(event):
    event.widget.config(bg="lightblue")

def bouton_leave(event):
    event.widget.config(bg="SystemButtonFace")

bouton_height = int(bandeau_height * 0.8)



def redirect_to_resa_avion():
    try:
        subprocess.Popen(["python", "resaAvionMembre.py"], shell=True)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")


bouton_vol = tk.Button(root, text="Achat Vol", width=15, command=redirect_to_resa_avion)
bouton_vol.place(x=bandeau_height * 4.6, y=bouton_height)
bouton_vol.bind('<Enter>', bouton_hover)
bouton_vol.bind('<Leave>', bouton_leave)


def redirect_to_connexion():
    try:
        subprocess.Popen(["python", "connexion.py"], shell=True)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")


bouton_connexion = tk.Button(root, text="Connexion", width=15, command=redirect_to_connexion)
bouton_connexion.place(x=bandeau_height * 5.4, y=bouton_height)
bouton_connexion.bind('<Enter>', bouton_hover)
bouton_connexion.bind('<Leave>', bouton_leave)

# Bouton "Créer son compte"
bouton_creer_compte = tk.Button(root, text="Créer son compte", width=15)
bouton_creer_compte.place(x=bandeau_height * 6.2, y=bouton_height)
bouton_creer_compte.bind('<Enter>', bouton_hover)
bouton_creer_compte.bind('<Leave>', bouton_leave)



# Redimensionner la liste déroulante
option_menu_width = 15
option_menu_height = 5
option_menu.config(width=option_menu_width, height=option_menu_height)
option_menu.place_forget()

#logo
image_path2 = "../Pictures/AirFly.png"
image2 = tk.PhotoImage(file=image_path2)
image2 = image2.subsample(5)  # Réduire l'image à 20% de sa taille d'origine
image_label2 = tk.Label(root, image=image2)
image_label2.place(x=bandeau_height * 0.7, y=bandeau_height * 0.1)

# fenêtre est redimensionnable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()