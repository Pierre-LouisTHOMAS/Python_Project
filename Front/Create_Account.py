import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform
from PIL import Image, ImageTk
import hashlib
import pymysql

import config

class Create_Account:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Page Create Account")

        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.menu = None

        self.create_window()

    def open_create_account_window(self):
        self.create_account_window = tk.Toplevel(self.root)
        self.create_account_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.create_account_window.title("Create an account")
        self.background_image = Image.open("../Pictures/bg3.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.create_account_window, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        image_path2 = "../Pictures/Logo.png"
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Create_Account(root)
    root.mainloop()