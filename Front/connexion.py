import tkinter as tk
from tkinter import messagebox
import mysql.connector
import platform

# Booléens pour le contrôle de l'application
is_logged_in = False

def run_login_window():
    global is_logged_in

    # Création de la fenêtre principale si l'utilisateur n'est pas connecté
    if not is_logged_in:
        root = tk.Tk()
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        root.configure(bg='white')  # Définir la couleur de fond en blanc
        root.title("Connexion")

        # Connexion à la base de données MySQL hébergée sur MAMP
        mydb = mysql.connector.connect(
            host="localhost",
            port=8889,
            user="root",
            password="root",
            database="AirlineDatabase"
        )
        cursor = mydb.cursor()

        # Hauteur du bandeau
        bandeau_height = root.winfo_screenheight() * 0.20

        # Bandeau en fond blanc
        canvas = tk.Canvas(root, bg="white")
        canvas.place(x=0, y=0, relwidth=1, relheight=0.20)  # Bandeau sur 20% de la hauteur

        # Fonction pour vérifier l'authenticité de l'utilisateur
        def check_login():
            global is_logged_in
            email = email_var.get()
            password = password_var.get()

            # Recherche de l'utilisateur dans la base de données
            cursor.execute("SELECT * FROM Client WHERE Email = %s AND Password = %s", (email, password))
            user = cursor.fetchone()

            # Vérification si l'utilisateur existe ou non
            if user:
                is_logged_in = True
                messagebox.showinfo("Succès", "Connexion réussie!")
                root.destroy()  # Fermer la fenêtre après une connexion réussie
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

        # La fenêtre est redimensionnable
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.mainloop()

        # Fermeture de la connexion à la base de données après la fermeture de la fenêtre
        cursor.close()
        mydb.close()

    # Sinon, exécuter le reste du programme ou afficher un message, etc.
    else:
        print("L'utilisateur est déjà connecté.")

# Exécuter la fenêtre de connexion
run_login_window()

# Code pour la suite de votre application
# Si l'utilisateur est connecté, vous pouvez continuer avec le reste de votre application ici.
# Vous pouvez utiliser les booléens définis au début pour contrôler le flux de votre programme.
