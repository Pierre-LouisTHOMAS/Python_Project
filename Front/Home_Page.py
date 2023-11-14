import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform
from PIL import Image, ImageTk
import hashlib
import pymysql

import config #global variables
import PlaneBooking
import EmployeePage

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
        self.root.title("SkyTravellers: Home Page")
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
        image_button_label.place(x=10, y=self.window_height * 0.06)
        image_button_label.bind("<Button-1>", self.create_menu)

        image_path3 = "../Pictures/Logo.png"
        self.image3 = tk.PhotoImage(file=image_path3)
        image_label3 = tk.Label(self.root, image=self.image3)
        image_label3.place(x=0, y=self.bandeau_height * 1.05, relwidth=1, relheight=0.75)

    def create_buttons(self):
        bouton_height = int(self.bandeau_height * 0.8)


        bouton_vol = tk.Button(self.root, text="Achat Vol", width=15, command=self.redirect_to_plane_booking)
        bouton_vol.place(x=self.window_width * 0.6, y=bouton_height)
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
        self.app = PlaneBooking.BookingApp(self.plane_booking_window)

    def redirect_to_home_page(self, event):
        self.connection_window.destroy()
        #self.create_account_window.destroy()

    def redirect_to_employee_page(self, event):
        self.employeePage_window = tk.Toplevel(self.root)
        self.app = EmployeePage.HomeEmployee(self.employeePage_window)


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
