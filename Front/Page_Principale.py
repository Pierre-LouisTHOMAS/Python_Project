import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform
from PIL import Image, ImageTk
import hashlib
import pymysql

import config #global variables

# Page Principale
class AIRENGLANDApp:
    def __init__(self, root):
        self.root = root

        # Initialisation de login_frame
        self.login_frame = tk.Frame(root, bg='grey', bd=5)
        self.login_frame.place_forget()  # Cachez initialement le cadre

        # Initialisation de email_label
        self.email_label = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.email_label.place(relx=0.1, rely=0.5)

        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND: Home Page")
        self.bandeau_height = root.winfo_screenheight() * 0.22
        self.menu = None
        self.bouton_connexion = None
        self.bouton_create_account = None

        self.create_bandeau()
        self.create_buttons()

        self.periodic_update()


    def create_bandeau(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        image_path = "../Pictures/barre_recherche.png"
        self.image_button = tk.PhotoImage(file=image_path)
        image_button_label = tk.Label(self.root, image=self.image_button, cursor="hand2")
        image_button_label.place(x=10, y=self.bandeau_height * 0.3)
        image_button_label.bind("<Button-1>", self.create_menu)

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

    def create_menu(self, event):
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None
        else:
            image_path = "../Pictures/barre_recherche.png"
            image_button_label = event.widget
            x, y = image_button_label.winfo_rootx(), image_button_label.winfo_rooty()

            self.menu = tk.Menu(self.root, tearoff=0)

            fichier_menu = tk.Menu(self.menu, tearoff=0)
            fichier_menu.add_command(label="Enregistrer sous...", command=self.save)
            fichier_menu.add_command(label="Enregistrer sous...", command=self.save)
            fichier_menu.add_command(label="Enregistrer sous...", command=self.save)

            self.menu.add_cascade(label="Fichier", menu=fichier_menu)

            self.menu.post(x, y)

    def bouton_hover(self, event):
        event.widget.config(bg="lightblue")

    def bouton_leave(self, event):
        event.widget.config(bg="SystemButtonFace")

    def save(self):
        print("Vous avez cliqué sur Enregistrer sous...")

    def redirect_to_resa_avion(self):
        root.destroy()
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "resaAvionMembre.py"], shell=True)
            else:
                subprocess.Popen(["python3", "resaAvionMembre.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")


    def redirect_to_create(self):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "Create_Account.py"], shell=True)
            else:
                subprocess.Popen(["python3", "Create_Account.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def open_connexion_window(self):
        self.connexion_window = tk.Toplevel(self.root)
        self.connexion_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.connexion_window.title("Connexion")

        # Widgets pour l'email
        email_label = tk.Label(self.connexion_window, text="Email")
        email_label.pack()
        self.email_entry = tk.Entry(self.connexion_window)
        self.email_entry.pack()

        # Widgets pour le mot de passe
        password_label = tk.Label(self.connexion_window, text="Password")
        password_label.pack()
        self.password_entry = tk.Entry(self.connexion_window, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self.connexion_window, text="Connexion", command=self.login)
        login_button.pack()

        login_button = tk.Button(self.connexion_window, text="Create an account", command=self.login)
        login_button.pack()

        # Message d'erreur
        self.error_label = tk.Label(self.connexion_window, text="", fg="red")
        self.error_label.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Remplacez ceci par votre propre logique de vérification de la connexion
        success, user_info = self.verify_login(email, password)

        if success:
            config.is_user_logged_in = True
            config.user_type, config.user_last_name, config.user_first_name, config.client_type = user_info
            self.connexion_window.destroy()  # Ferme uniquement la fenêtre de connexion
            self.update_ui()
            self.periodic_update()
        else:
            self.error_label.config(text="Email ou mot de passe incorrect!")
    def verify_login(self, email, password):
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


# Create account
    def open_create_account_window(self):
        self.create_account_window = tk.Toplevel(self.root)
        #self.connexion_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.create_account_window.title("Create an account")

        # Cadre pour le formulaire de création de compte
        account_frame = tk.Frame(root, bg='white', bd=5)
        account_frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8, anchor='center')

        # Style pour les labels et les entrées
        label_font = ('Verdana', 12)
        entry_font = ('Verdana', 12)
        button_font = ('Verdana', 12, 'bold')

        # First name
        tk.Label(account_frame, text="First name", font=label_font, bg='black').pack(pady=10)
        first_name_entry = tk.Entry(account_frame, font=entry_font)
        first_name_entry.pack(fill='x', padx=50)

        # Last name
        tk.Label(account_frame, text="Last name", font=label_font, bg='black').pack(pady=10)
        last_name_entry = tk.Entry(account_frame, font=entry_font)
        last_name_entry.pack(fill='x', padx=50)

        # Category
        tk.Label(account_frame, text="Category", font=label_font, bg='black').pack(pady=10)
        category_var = tk.StringVar(value="regular")  # default value
        category_option_menu = ttk.OptionMenu(account_frame, category_var, "regular", "regular", "senior", "child")
        category_option_menu.pack(fill='x', padx=50)

        # Email
        tk.Label(account_frame, text="Email", font=label_font, bg='black').pack(pady=10)
        email_entry = tk.Entry(account_frame, font=entry_font)
        email_entry.pack(fill='x', padx=50)

        # Password
        tk.Label(account_frame, text="Password", font=label_font, bg='black').pack(pady=10)
        password_entry = tk.Entry(account_frame, font=entry_font, show="*")
        password_entry.pack(fill='x', padx=50)
        # Par exemple, des Entry pour le prénom, le nom, l'email, etc.

    def email_exists(self, email):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM user WHERE Email = %s"
                cursor.execute(sql, (email,))
                return cursor.fetchone() is not None
        except Exception as e:
            messagebox.showerror("Erreur", f"Database error: {e}")
            return False
        finally:
            conn.close()
    def insert_client(self, first_name, last_name, client_type, category, email, password):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        try:
            with conn.cursor() as cursor:
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                sql = "INSERT INTO User (First_Name, Last_Name, Category, Email, Password) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (first_name, last_name, client_type, category, email,
                                     password))  # remplacer password par hashed_password
            conn.commit()
        except Exception as e:
            messagebox.showerror("Erreur", f"Database error: {e}")
        finally:
            conn.close()
    def create_account(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        category = self.category_var.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if self.email_exists(email):
            messagebox.showerror("Erreur", "Email already exists!")
            return

        self.insert_client(first_name, last_name, category, email, password)
        messagebox.showinfo("Success", "Account created successfully!")
        self.create_account_window.destroy()



#Update appication
    def update_ui(self):
        if config.is_user_logged_in:
            if config.user_type == 'client':
                user_info_text = f"Client: {config.user_first_name} {config.user_last_name}\nType: {config.client_type}"
            elif config.user_type == 'employe':
                user_info_text = f"Employé: {config.user_first_name} {config.user_last_name}"
            else:
                user_info_text = "Utilisateur connecté"

            self.login_frame.place(relx=1, rely=0, relwidth=0.25, relheight=0.1, anchor='ne')
            self.email_label.config(text=user_info_text)

            if self.bouton_connexion is not None:
                self.bouton_connexion.destroy()
                self.bouton_connexion = None
            if self.bouton_create_account is not None:
                self.bouton_create_account.destroy()
                self.bouton_create_account = None

        else:
            if self.bouton_connexion is None:
                self.bouton_connexion = tk.Button(self.root, text="Connexion", width=15, command=self.open_connexion_window)
                self.bouton_connexion.place(x=self.bandeau_height * 5.4, y=self.bandeau_height * 0.8)
                self.bouton_connexion.bind('<Enter>', self.bouton_hover)
                self.bouton_connexion.bind('<Leave>', self.bouton_leave)
            if self.bouton_create_account is None:
                self.bouton_creer_compte = tk.Button(self.root, text="Create an account", width=15,command=self.redirect_to_create)
                self.bouton_creer_compte.place(x=self.bandeau_height * 6.2, y=self.bandeau_height * 0.8)
                self.bouton_creer_compte.bind('<Enter>', self.bouton_hover)
                self.bouton_creer_compte.bind('<Leave>', self.bouton_leave)

    def periodic_update(self):
        self.update_ui()
        self.root.after(1000, self.periodic_update)


if __name__ == "__main__":
    root = tk.Tk()
    app = AIRENGLANDApp(root)

    root.mainloop()
