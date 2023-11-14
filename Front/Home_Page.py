import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform
from PIL import Image, ImageTk
import hashlib
import pymysql

import config #global variables
import PlaneBooking

# Home Page
class HomePageApp:
    def __init__(self, root):
        self.root = root
        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        # Initialisation de login_frame
        self.login_frame = tk.Frame(root, bg='grey', bd=5)
        self.login_frame.place_forget()  # Cachez initialement le cadre

        # Initialisation de email_label
        self.email_label = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.email_label.place(relx=0.1, rely=0.5)


        # Initialisation of first_name_label_create_account
        self.first_name_label_create_account = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.first_name_label_create_account.place(relx=0.1, rely=0.5)

        # Initialisation of last_name_label_create_account
        self.last_name_label_create_account = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.last_name_label_create_account.place(relx=0.1, rely=2.5)

        # Initialisation of category_label_create_account
        self.category_label_create_account = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.category_label_create_account.place(relx=0.1, rely=4.5)

        # Initialisation of email_label_create_account
        self.email_label_create_account = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.email_label_create_account.place(relx=0.1, rely=6.5)

        # Initialisation of password_label_create_account
        self.password_label_create_account = tk.Label(self.login_frame, font=('Helvetica', 12), bg='black')
        self.password_label_create_account.place(relx=0.1, rely=8.5)

        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND: Home Page")
        self.bandeau_height = root.winfo_screenheight() * 0.22
        self.menu = None

        # For update_ui()
        self.bouton_connection = None
        self.bouton_create_account = None
        self.type_var = tk.StringVar(value="Member")  # Déplacez cette ligne dans __init__

        self.space_type_var = None

        self.create_header()
        self.create_buttons()

        self.periodic_update()


    def create_header(self):
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


        bouton_vol = tk.Button(self.root, text="Achat Vol", width=15, command=self.redirect_to_plane_booking)
        bouton_vol.place(x=self.bandeau_height * 4.4, y=bouton_height)
        bouton_vol.bind('<Enter>', self.bouton_hover)
        bouton_vol.bind('<Leave>', self.bouton_leave)

    def create_menu(self, event):
        image_button_label = event.widget
        x, y = image_button_label.winfo_rootx(), image_button_label.winfo_rooty()

        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Historique", command=self.save)
        menu.add_command(label="Facture", command=self.save)
        menu.post(x, y)

    def bouton_hover(self, event):
        event.widget.config(bg="lightblue")

    def bouton_leave(self, event):
        event.widget.config(bg="SystemButtonFace")

    def save(self):
        print("Vous avez cliqué sur Enregistrer sous...")

    def redirect_to_plane_booking(self):
        self.plane_booking_window = tk.Toplevel(self.root)
        self.plane_booking_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.plane_booking_window.title("Plane Booking")
        self.app = PlaneBooking.BookingApp(self.plane_booking_window)

    def redirect_to_home_page(self, event):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "Home_Page.py"], shell=True)
            else:
                subprocess.Popen(["python3", "Home_Page.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def redirect_to_employee_page(self, event):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "EmployeePage.py"], shell=True)
            else:
                subprocess.Popen(["python3", "EmployeePage.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def open_connection_window(self):
        self.connection_window = tk.Toplevel(self.root)
        self.connection_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.connection_window.title("Connection")

        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.connection_window, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.connection_window, image=self.image2)
        image_label2.place(x=self.header_height * 0.4, y=self.header_height * 0.3)

        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))

        form_frame = tk.Frame(self.connection_window, bg="white")
        form_frame.place(relx=0.75, rely=0.5, anchor="center", relwidth=0.2, relheight=0.4)

        email_label = tk.Label(form_frame, text="Email")
        email_label.pack(pady=(10 , 2))
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.pack(fill='x', padx=10, pady=2)

        password_label = tk.Label(form_frame, text="Password")
        password_label.pack(pady=(10, 2))
        self.password_entry = tk.Entry(form_frame, show="*")
        self.password_entry.pack(fill='x', padx=10, pady=2)

        login_button = tk.Button(form_frame, text="connection", command=self.login)
        login_button.pack(pady=10)

        create_account_button = tk.Button(form_frame, text="Create an account", command=self.open_create_account_window)
        create_account_button.pack()

        self.error_label = tk.Label(form_frame, text="", fg="red")
        self.error_label.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        success, user_info = self.verify_login(email, password)

        if success:
            config.is_user_logged_in = True
            config.first_name_user = user_info['First_Name']
            config.last_name_user = user_info['Last_Name']
            config.user_type = user_info['Type']
            config.member_category = user_info['Category']
            self.connection_window.destroy()  # Ferme uniquement la fenêtre de connection
            self.update_ui()
            self.periodic_update()
            if config.user_type == 'Employee':
                self.redirect_to_employee_page(self)
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
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

                cursor.execute("SELECT First_Name, Last_Name, Type, Category FROM User WHERE email = %s AND password = %s", (email, hashed_password))
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
        self.create_account_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.create_account_window.title("Create an account")

        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.create_account_window, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)


        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.create_account_window, image=self.image2)
        image_label2.place(x=self.header_height * 0.4, y=self.header_height * 0.3)

        # Return to home page
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))

        self.account_frame = tk.Frame(self.create_account_window, bg='gray', bd=5)
        self.account_frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.75, anchor='center')

        label_font = ('Verdana', 14, 'bold')
        entry_font = ('Verdana', 12)
        button_font = ('Verdana', 12, 'bold')

        # First name
        tk.Label(self.account_frame, text="First name", font=label_font, bg='white').pack(pady=10)
        self.first_name_entry = tk.Entry(self.account_frame, font=entry_font)
        self.first_name_entry.pack(fill='x', padx=50)

        # Last name
        tk.Label(self.account_frame, text="Last name", font=label_font, bg='white').pack(pady=10)
        self.last_name_entry = tk.Entry(self.account_frame, font=entry_font)
        self.last_name_entry.pack(fill='x', padx=50)

        # Type
        tk.Label(self.account_frame, text="Type", font=label_font, bg='white').pack(pady=10)
        self.type_var = tk.StringVar(value="Member")  # valeur par défaut
        self.type_option_menu = ttk.OptionMenu(self.account_frame, self.type_var, "Member", "Member",
                                               "Employee", command=self.toggle_category_code_fields)
        self.type_option_menu.pack(fill='x', padx=50)

        self.category_label = tk.Label(self.account_frame, text="Category", font=label_font, bg='white')
        self.category_var = tk.StringVar(value="regular")
        self.category_option_menu = ttk.OptionMenu(self.account_frame, self.category_var, "regular", "regular","senior", "child")

        self.code_label = tk.Label(self.account_frame, text="Code")
        self.code_entry = tk.Entry(self.account_frame, show="*")

        self.toggle_category_code_fields("Member")

        # Email
        tk.Label(self.account_frame, text="Email", font=label_font, bg='white').pack(pady=10)
        self.email_entry = tk.Entry(self.account_frame, font=entry_font)
        self.email_entry.pack(fill='x', padx=50)

        # Password
        tk.Label(self.account_frame, text="Password", font=label_font, bg='white').pack(pady=10)
        self.password_entry = tk.Entry(self.account_frame, font=entry_font, show="*")
        self.password_entry.pack(fill='x', padx=50)
        login_button = tk.Button(self.account_frame, text="Create an account", command=self.create_account, font=button_font, relief=tk.FLAT, bg='#4CAF50', fg='black')
        login_button.pack(pady=5)

        # Message d'erreur
        self.error_label = tk.Label(self.account_frame, text="", fg="red")
        self.error_label.pack(pady=20)

    def toggle_category_code_fields(self, *args):
        selected_type = self.type_var.get()
        if selected_type == "Employee":
            # Afficher Code, cacher Category
            self.category_label.pack_forget()
            self.category_option_menu.pack_forget()
            self.code_label.pack(pady=10)
            self.code_entry.pack(fill='x', padx=50)
        else:
            # Afficher Category, cacher Code
            self.code_label.pack_forget()
            self.code_entry.pack_forget()
            self.category_label.pack(pady=10)
            self.category_option_menu.pack(fill='x', padx=50)
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
            self.error_label.config(text=f"Database error: {e}")
            return False
        finally:
            conn.close()
    def insert_client(self, first_name, last_name, type, category, email, password):
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
                sql = "INSERT INTO User (First_Name, Last_Name, Type, Category, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (first_name, last_name, type, category, email, hashed_password)) # remplacer password par hashed_password
            conn.commit()
        except Exception as e:
            self.error_label.config(text=f"Database error: {e}")
            return
        finally:
            conn.close()
    def create_account(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        type = self.type_var.get()
        code = self.code_entry.get()
        category = self.category_var.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.email_exists(email):
            self.error_label.config(text="Email already exists!")
            return
        if not first_name or not last_name or not category or not email or not password:
            self.error_label.config(text="Please enter all fields")
            return
        if type == 'Employee' and code != '12':
            self.error_label.config(text="You are not a Employee")
            return
        self.insert_client(first_name, last_name, type, category, email, password)
        messagebox.showinfo("Success", "Account created successfully!")
        self.create_account_window.destroy()


#Update appication
    def update_ui(self):
        if config.is_user_logged_in:
            if self.bouton_connection is not None:
                self.bouton_connection.destroy()
                self.bouton_connection = None
            if self.bouton_create_account is not None:
                self.bouton_create_account.destroy()
                self.bouton_create_account = None
        else:
            if self.bouton_connection is None:
                self.bouton_connection = tk.Button(self.root, text="Connection", width=15, command=self.open_connection_window)
                self.bouton_connection.place(x=self.bandeau_height * 5.3, y=self.bandeau_height * 0.8)
                self.bouton_connection.bind('<Enter>', self.bouton_hover)
                self.bouton_connection.bind('<Leave>', self.bouton_leave)
            if self.bouton_create_account is None:
                self.bouton_create_account = tk.Button(self.root, text="Create an account", width=15,command=self.open_create_account_window)
                self.bouton_create_account.place(x=self.bandeau_height * 6.2, y=self.bandeau_height * 0.8)
                self.bouton_create_account.bind('<Enter>', self.bouton_hover)
                self.bouton_create_account.bind('<Leave>', self.bouton_leave)

    def periodic_update(self):
        self.update_ui()
        self.root.after(500, self.periodic_update)



if __name__ == "__main__":
    root = tk.Tk()
    app = HomePageApp(root)

    root.mainloop()
