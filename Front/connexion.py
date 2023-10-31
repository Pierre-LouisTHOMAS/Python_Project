import tkinter as tk
from tkinter import messagebox
import sqlite3

# Création de la fenêtre principale
root = tk.Tk()
root.title("Connexion")

# Connexion à la base de données SQLite
conn = sqlite3.connect('../Back/Test_Records.sql')
cursor = conn.cursor()


# Fonction pour vérifier l'authenticité de l'utilisateur
def check_login():
    email = email_var.get()
    password = password_var.get()

    # Recherche de l'utilisateur dans la base de données
    cursor.execute("SELECT * FROM Client WHERE Email = ? AND Password = ?", (email, password))
    user = cursor.fetchone()

    # Vérification si l'utilisateur existe ou non
    if user:
        messagebox.showinfo("Succès", "Connexion réussie!")
    else:
        messagebox.showerror("Erreur", "Email ou mot de passe incorrect!")


# Création des éléments de la fenêtre
label1 = tk.Label(root, text="Email")
label1.pack(pady=10)

email_var = tk.StringVar()
entry_email = tk.Entry(root, textvariable=email_var)
entry_email.pack(pady=10)

label2 = tk.Label(root, text="Mot de passe")
label2.pack(pady=10)

password_var = tk.StringVar()
entry_password = tk.Entry(root, textvariable=password_var, show='*')
entry_password.pack(pady=10)

btn_login = tk.Button(root, text="Se connecter", command=check_login)
btn_login.pack(pady=20)

root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
