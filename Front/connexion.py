import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Assurez-vous d'installer le module pillow

import subprocess
import platform
import hashlib
import pymysql

import config #global variables

def verify_login(email, password):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='AirlineDatabase',
        port=8889
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT First_Name, Last_Name, Type, Category FROM User WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()
            if result:
                # Créer un dictionnaire avec les informations de l'utilisateur
                user_info = {
                    'First_Name': result[0],
                    'Last_Name': result[1],
                    'Type': result[2],
                    'Category': result[3]
                }
                return True, user_info
            else:
                return False, None
    except Exception as e:
        messagebox.showerror("Erreur", f"Database error: {e}")
        return False, None
    finally:
        conn.close()

def login():
    email = email_entry.get()
    password = password_entry.get()

    success, user_info = verify_login(email, password)

    if success:
        config.is_user_logged_in = True
        config.user_type, config.user_last_name, config.user_first_name, config.client_type = user_info

        print(f"Logged in: {config.is_user_logged_in}, User Type: {config.user_type}")
        root.destroy()
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "Page_Principale.py"], shell=True)
            else:
                subprocess.Popen(["python3", "Page_Principale.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")
    else:
        error_label.config(text="Email ou mot de passe incorrect!", fg="red")


# Configuration de la fenêtre principale
root = tk.Tk()
root.configure(bg='black')
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Connexion")

# Configuration de l'image de fond
background_image = Image.open("../Pictures/Boreale.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Cadre pour le formulaire de connexion
login_frame = tk.Frame(root, bg='white', bd=5)
login_frame.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.3, anchor='center')

# Widgets pour l'email
email_label = tk.Label(login_frame, text="Email", font=('Helvetica', 12), bg='white')
email_label.place(relx=0.5, rely=0.1, anchor='center')
email_entry = tk.Entry(login_frame, font=('Helvetica', 12))
email_entry.place(relx=0.5, rely=0.2, relwidth=0.7, anchor='center')

# Widgets pour le mot de passe
password_label = tk.Label(login_frame, text="Mot de passe", font=('Helvetica', 12), bg='white')
password_label.place(relx=0.5, rely=0.35, anchor='center')
password_entry = tk.Entry(login_frame, font=('Helvetica', 12), show="*")
password_entry.place(relx=0.5, rely=0.45, relwidth=0.7, anchor='center')

# Bouton de connexion
login_button = tk.Button(login_frame, text="Se connecter", command=login, font=('Helvetica', 12))
login_button.place(relx=0.5, rely=0.7, relwidth=0.7, anchor='center')

def redirect_to_create_account():
    root.destroy()

    try:
        if platform.system() == 'Windows':
            subprocess.Popen(["python", "Create_Account.py"], shell=True)
        else:
            subprocess.Popen(["python3", "Create_Account.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")

# Bouton pour créer un compte
create_account_button = tk.Button(login_frame, text="Créer un compte", command=redirect_to_create_account, font=('Helvetica', 12))
create_account_button.place(relx=0.5, rely=0.85, relwidth=0.7, anchor='center')

# Message d'erreur
error_label = tk.Label(root, text="", font=('Helvetica', 12), bg='white')
error_label.place(relx=0.5, rely=0.85, anchor='center')

root.mainloop()