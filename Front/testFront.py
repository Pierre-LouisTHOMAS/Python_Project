from tkinter import *

fenetre = Tk()
fenetre.geometry('400x400')
fenetre['bg']= 'red'

def save():
    print("vous avez cliqué")
mon_menu = Menu(fenetre)

#Sous onglet
fichier = Menu(mon_menu, tearoff=0)
fichier.add_command(label="Enregistrer sous...", command=save)

option = Menu(mon_menu, tearoff=0)
option.add_command(label="reglage")
#les 2 principaux onglets(configuration)
mon_menu.add_cascade(label="fichier", menu=fichier)
mon_menu.add_cascade(label="option", menu=option)

fenetre.config(menu=mon_menu)


fenetre.mainloop()