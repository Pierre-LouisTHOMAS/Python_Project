import tkinter as tk
from tkcalendar import DateEntry # A telecharger PL
from tkinter import Label

# Création de la fenêtre principale
root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Réservation de Vol")

# Hauteur du bandeau
bandeau_height = root.winfo_screenheight() * 0.20

# Bandeau en fond blanc
canvas = tk.Canvas(root, bg="white")
canvas.place(x=0, y=0, relwidth=1, relheight=0.20)  # Bandeau sur 20% de la hauteur

#logo
image_path2 = "../Pictures/AirFly.png"
image2 = tk.PhotoImage(file=image_path2)
image2 = image2.subsample(5)  # Réduire l'image à 20% de sa taille d'origine
image_label2 = tk.Label(root, image=image2)
image_label2.place(x=bandeau_height * 0.7, y=bandeau_height * 0.1)

# Création d'un cadre principal pour centrer les éléments en dehors du bandeau
main_frame = tk.Frame(root, relief="solid", borderwidth=2)
main_frame.grid(row=1, column=0, padx=10, pady=10)

# Titre
title_label = tk.Label(main_frame, text="Recherche de Vol", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Date de départ
date_label = tk.Label(main_frame, text="Date de Départ")
date_label.grid(row=1, column=0, pady=5)
date_var = tk.StringVar()
date_entry = DateEntry(main_frame, textvariable=date_var, date_pattern="dd/mm/yyyy")#modifier ici si tu peux pas recup l'info
date_entry.grid(row=1, column=1, pady=5)

# Aéroport de départ
departure_label = tk.Label(main_frame, text="Aéroport de Départ")
departure_label.grid(row=2, column=0, pady=5)
departure_var = tk.StringVar()
departure_entry = tk.Entry(main_frame, textvariable=departure_var)
departure_entry.grid(row=2, column=1, pady=5)

# Aéroport d'arrivée
arrival_label = tk.Label(main_frame, text="Aéroport d'Arrivée")
arrival_label.grid(row=3, column=0, pady=5)
arrival_var = tk.StringVar()
arrival_entry = tk.Entry(main_frame, textvariable=arrival_var)
arrival_entry.grid(row=3, column=1, pady=5)

# Type de personne
person_type_label = tk.Label(main_frame, text="Type de Personne")
person_type_label.grid(row=4, column=0, pady=5)
person_type_var = tk.StringVar()
person_type_var.set("Adulte")  # Par défaut, on sélectionne "Adulte"
person_type_option = tk.OptionMenu(main_frame, person_type_var, "Adulte", "Enfant")
person_type_option.grid(row=4, column=1, pady=5)



search_button = tk.Button(main_frame, text="Rechercher des Vols")
search_button.grid(row=6, column=0, columnspan=2, pady=10)

# Ajout de l'image à droite de l'encadré
image_path = "../Pictures/avionResa.png"
image = tk.PhotoImage(file=image_path)
image = image.subsample(2)  # Réduire l'image de 50% (vous pouvez ajuster le facteur de réduction)
image_label = Label(main_frame, image=image)
image_label.grid(row=0, column=2, rowspan=7, padx=10)

# fenêtre est redimensionnable
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)  # Ajustez la ligne 1

root.mainloop()
