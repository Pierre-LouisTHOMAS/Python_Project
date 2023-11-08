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


#autre solution de create_menu
def create_menu(self, event):
    image_button_label = event.widget
    x, y = image_button_label.winfo_rootx(), image_button_label.winfo_rooty()

    menu = tk.Menu(self.root, tearoff=0)
    menu.add_command(label="Enregistrer sous...", command=self.save)
    menu.post(x, y)


fenetre.mainloop()