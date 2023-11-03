import tkinter as tk
from tkinter import *

# Création de la fenêtre principale
root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("AIRENGLAND")

# Hauteur du bandeau
bandeau_height = root.winfo_screenheight() * 0.25

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

# Ajouter un canvas avec un fond blanc en tant que bandeau
canvas = tk.Canvas(root, bg="white")
canvas.place(x=0, y=0, relwidth=1, relheight=0.25)  # Positionne le canvas sur 25% de la hauteur

# Créer un bouton image pour afficher/masquer la liste déroulante
image_path = "../Pictures/barre_recherche.png"
image_button = tk.PhotoImage(file=image_path)
image_button = image_button.subsample(2)  # Redimensionner l'image
image_button_label = tk.Label(root, image=image_button, cursor="hand2")
image_button_label.place(x=10, y=bandeau_height * 0.05)
image_button_label.bind("<Button-1>", lambda e: toggle_dropdown())

# Ajouter une liste déroulante (OptionMenu) initialement masquée
choices = ["Connexion", "Premium Economy", "Economy"]
var = tk.StringVar(root)
var.set(choices[0])
option_menu = tk.OptionMenu(root, var, *choices)

# Ajouter une image en tant que label
image_path = "../Pictures/Boreale.png"
image = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=image)
# Positionner l'image pour couvrir toute la largeur de la fenêtre
image_label.place(x=0, y=bandeau_height * 1.05, relwidth=1, relheight=0.75)


def bouton_hover(event):
    event.widget.config(bg="lightblue")

def bouton_leave(event):
    event.widget.config(bg="SystemButtonFace")

bouton_height = int(bandeau_height * 0.8)

# Bouton "Connexion"
bouton_connexion = tk.Button(root, text="Connexion", width=15)
bouton_connexion.place(x=bandeau_height * 5.3, y=bouton_height)
bouton_connexion.bind('<Enter>', bouton_hover)  # Associez la fonction bouton_hover à l'événement de survol
bouton_connexion.bind('<Leave>', bouton_leave)  # Associez la fonction bouton_leave à l'événement de départ

# Bouton "Créer son compte"
bouton_creer_compte = tk.Button(root, text="Créer son compte", width=15)
bouton_creer_compte.place(x=bandeau_height * 6, y=bouton_height)
bouton_creer_compte.bind('<Enter>', bouton_hover)  # Associez la fonction bouton_hover à l'événement de survol
bouton_creer_compte.bind('<Leave>', bouton_leave)  # Associez la fonction bouton_leave à l'événement de départ


# Bouton "Créer son compte"
bouton_vol = tk.Button(root, text="Achat_Vol", width=15)
bouton_vol.place(x=bandeau_height * 4.5, y=bouton_height)
bouton_vol.bind('<Enter>', bouton_hover)
bouton_vol.bind('<Leave>', bouton_leave)

# Redimensionner la liste déroulante
option_menu_width = 15  # Largeur souhaitée de la liste déroulante
option_menu_height = 5  # Hauteur souhaitée de la liste déroulante
option_menu.config(width=option_menu_width, height=option_menu_height)
option_menu.place_forget()  # Masquer initialement la liste déroulante

# Ajouter une autre image en premier plan (au format JPG) dans le bandeau supérieur
image_path2 = "../Pictures/LogoBis.png"
image2 = tk.PhotoImage(file=image_path2)
image2 = image2.subsample(5)  # Réduire l'image à 20% de sa taille d'origine
image_label2 = tk.Label(root, image=image2)
image_label2.place(x=bandeau_height * 0.7, y=bandeau_height * 0.1)  # Décalage de 20% de la longueur et 5% vers le bas

# Assurez-vous que la fenêtre est redimensionnable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
