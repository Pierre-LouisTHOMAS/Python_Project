import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform
from PIL import Image, ImageTk
import hashlib
import pymysql

import config

class Connection:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Connection Page")

        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.menu = None

        self.create_window()

    def open_connection_window(self):
        self.connection_window = tk.Toplevel(self.root)
        self.connection_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.connection_window.title("Connection")
        self.background_image = Image.open("../Pictures/bg2.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.connection_window, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)
        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.connection_window, image=self.image2)
        image_label2.place(x=self.header_height * 0.4, y=self.header_height * 0.3)
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))

        form_frame = tk.Frame(self.connection_window, bg="white")
        form_frame.place(relx=0.75, rely=0.5, anchor="center", relwidth=0.2, relheight=0.4)
        email_label = tk.Label(form_frame, text="Email")
        email_label.pack(pady=(10, 2))
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
                cursor.execute(
                    "SELECT First_Name, Last_Name, Type, Category FROM User WHERE email = %s AND password = %s",
                    (email, hashed_password))
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

        print("Payment button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = Connection(root)
    root.mainloop()