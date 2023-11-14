import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, ttk, messagebox
from PIL import Image, ImageTk

import config

class EmployeeAccount:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND:flight booking")

        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.image2 = None
        self.image = None

        self.create_window()

    def redirect_to_home_page(self, event):
        root.destroy()



    def create_window(self):
        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        # Configure columns and rows to make them expandable
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        self.main_frame = tk.Frame(self.root, relief="solid", borderwidth=2)
        self.main_frame.grid(row=1, column=1, padx=150, pady=15, sticky="e")

        # logo picture
        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.header_height * 0.7, y=self.header_height * 0.1)

        # Return to home page
        image_label2.bind("<Button-1>", self.redirect_to_home_page)

        title_label = tk.Label(self.main_frame, text="Employee Account", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        user_name_label = tk.Label(self.main_frame, text="Name:")
        user_name_label.grid(row=3, column=0, pady=5)
        user_name_entry = tk.Entry(self.main_frame)
        user_name_entry.grid(row=3, column=1, pady=5)

        user_surname_label = tk.Label(self.main_frame, text="Surname:")
        user_surname_label.grid(row=4, column=0, pady=5)
        user_surname_entry = tk.Entry(self.main_frame)
        user_surname_entry.grid(row=4, column=1, pady=5)

        user_email_label = tk.Label(self.main_frame, text="Email:")
        user_email_label.grid(row=1, column=0, pady=5)
        user_email_entry = tk.Entry(self.main_frame)
        user_email_entry.grid(row=1, column=1, pady=5)

        user_password_label = tk.Label(self.main_frame, text="Password:")
        user_password_label.grid(row=2, column=0, pady=5)
        user_password_entry = tk.Entry(self.main_frame, show="*")
        user_password_entry.grid(row=2, column=1, pady=5)

        image_path = "../Pictures/AccountPicture.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(4)
        image_label = Label(self.main_frame, image=self.image)
        image_label.grid(row=0, column=2, rowspan=7, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeAccount(root)
    root.mainloop()
