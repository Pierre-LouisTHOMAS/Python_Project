import tkinter as tk
from tkinter import messagebox, ttk
import pymysql
import hashlib
from PIL import Image, ImageTk

import subprocess
import platform

def email_exists(email):
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

def insert_client(first_name, last_name, client_type, category, email, password):
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
            cursor.execute(sql, (first_name, last_name, client_type, category, email, password)) # remplacer password par hashed_password
        conn.commit()
    except Exception as e:
        messagebox.showerror("Erreur", f"Database error: {e}")
    finally:
        conn.close()


def create_account():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    category = category_var.get()
    email = email_entry.get()
    password = password_entry.get()

    if email_exists(email):
        messagebox.showerror("Erreur", "Email already exists!")
        return

    insert_client(first_name, last_name, category, email, password)
    messagebox.showinfo("Success", "Account created successfully!")
    root.destroy()


# Configuration de la fenêtre principale
root = tk.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Create an account")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/4 - window_width / 4)
center_y = int(screen_height/4 - window_height / 4)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Configuration de l'image de fond
background_image = Image.open("../Pictures/Boreale.png")
background_photo = ImageTk.PhotoImage(background_image.resize((window_width, window_height), Image.LANCZOS))
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Cadre pour le formulaire de création de compte
account_frame = tk.Frame(root, bg='gray', bd=5)
account_frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.65, anchor='center')

# Style pour les labels et les entrées
label_font = ('Verdana', 14, 'bold')
entry_font = ('Verdana', 12)
button_font = ('Verdana', 12, 'bold')

# First name
tk.Label(account_frame, text="First name", font=label_font, bg='white').pack(pady=10)
first_name_entry = tk.Entry(account_frame, font=entry_font)
first_name_entry.pack(fill='x', padx=50)

# Last name
tk.Label(account_frame, text="Last name", font=label_font, bg='white').pack(pady=10)
last_name_entry = tk.Entry(account_frame, font=entry_font)
last_name_entry.pack(fill='x', padx=50)

# Category
tk.Label(account_frame, text="Category", font=label_font, bg='white').pack(pady=10)
category_var = tk.StringVar(value="regular")  # default value
category_option_menu = ttk.OptionMenu(account_frame, category_var, "regular", "regular", "senior", "child")
category_option_menu.pack(fill='x', padx=50)

# Email
tk.Label(account_frame, text="Email", font=label_font, bg='white').pack(pady=10)
email_entry = tk.Entry(account_frame, font=entry_font)
email_entry.pack(fill='x', padx=50)

# Password
tk.Label(account_frame, text="Password", font=label_font, bg='white').pack(pady=10)
password_entry = tk.Entry(account_frame, font=entry_font, show="*")
password_entry.pack(fill='x', padx=50)

def redirect_to_principal():
    root.destroy()
    try:
        if platform.system() == 'Windows':
            subprocess.Popen(["python", "Page_Principale.py"], shell=True)
        else:
            subprocess.Popen(["python3", "Page_Principale.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Error redirecting : {e}")

# Submit button
submit_button = tk.Button(account_frame, text="Create an account", command=redirect_to_principal, font=button_font, relief=tk.FLAT, bg='#4CAF50', fg='black')
submit_button.pack(pady=20)

root.mainloop()
