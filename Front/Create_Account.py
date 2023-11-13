import tkinter as tk
from tkinter import messagebox, ttk
import pymysql
import hashlib
from PIL import Image, ImageTk
import subprocess
import platform

class CreateAccountWindow:
    def __init__(self, root):
        self.root = root
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        self.create_widgets()

    def create_widgets(self):
        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        self.account_frame = tk.Frame(self.root, bg='gray', bd=5)
        self.account_frame.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.65, anchor='center')

        label_font = ('Verdana', 14, 'bold')
        entry_font = ('Verdana', 12)
        button_font = ('Verdana', 12, 'bold')

        tk.Label(self.account_frame, text="First name", font=label_font, bg='white').pack(pady=10)
        self.first_name_entry = tk.Entry(self.account_frame, font=entry_font)
        self.first_name_entry.pack(fill='x', padx=50)

        tk.Label(self.account_frame, text="Last name", font=label_font, bg='white').pack(pady=10)
        self.last_name_entry = tk.Entry(self.account_frame, font=entry_font)
        self.last_name_entry.pack(fill='x', padx=50)

        tk.Label(self.account_frame, text="Category", font=label_font, bg='white').pack(pady=10)
        self.category_var = tk.StringVar(value="regular")
        category_option_menu = ttk.OptionMenu(self.account_frame, self.category_var, "regular", "regular", "senior", "child")
        category_option_menu.pack(fill='x', padx=50)

        tk.Label(self.account_frame, text="Email", font=label_font, bg='white').pack(pady=10)
        self.email_entry = tk.Entry(self.account_frame, font=entry_font)
        self.email_entry.pack(fill='x', padx=50)

        tk.Label(self.account_frame, text="Password", font=label_font, bg='white').pack(pady=10)
        self.password_entry = tk.Entry(self.account_frame, font=entry_font, show="*")
        self.password_entry.pack(fill='x', padx=50)

        submit_button = tk.Button(self.account_frame, text="Create an account", command=self.redirect_to_home, font=button_font, relief=tk.FLAT, bg='#4CAF50', fg='black')
        submit_button.pack(pady=20)

    def redirect_to_home(self):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "Home_Page.py"], shell=True)
            else:
                subprocess.Popen(["python3", "Home_Page.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error redirecting: {e}")

root = tk.Tk()
app = CreateAccountWindow(root)
root.mainloop()
