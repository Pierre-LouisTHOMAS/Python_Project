import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, ttk, messagebox
import subprocess
import platform
from PIL import Image, ImageTk

import pymysql
import config
import FlightBooking

class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND:Plane booking")

        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.image2 = None
        self.image = None

        self.departure_var = tk.StringVar()
        self.arrival_var = tk.StringVar()

        self.create_window()

    def redirect_to_home_page(self, event):
            self.root.destroy()

    def create_window(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT DISTINCT Departure_Airport FROM Flight")
        departure_airports = [airport['Departure_Airport'] for airport in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT Arrival_Airport FROM Flight")
        arrival_airports = [airport['Arrival_Airport'] for airport in cursor.fetchall()]

        #background picture
        self.background_image = Image.open("../Pictures/bg4.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)
        self.main_frame = tk.Frame(self.root, relief="solid", borderwidth=2)
        self.main_frame.grid(row=1, column=0, padx=15, pady=15)

        # logo picture
        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.header_height * 0.7, y=self.header_height * 0.1)

        # Return to home page
        image_label2.bind("<Button-1>", self.redirect_to_home_page)

        title_label = tk.Label(self.main_frame, text="Flight Research", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        date_label = tk.Label(self.main_frame, text="Departure Date")
        date_label.grid(row=1, column=0, pady=5)
        self.date_var = tk.StringVar()
        date_entry = DateEntry(self.main_frame, textvariable=self.date_var, date_pattern="dd/mm/yyyy")
        date_entry.grid(row=1, column=1, pady=5)

        # Show only Departure Airport that exist in the database
        departure_label = tk.Label(self.main_frame, text="Departure airport")
        departure_label.grid(row=2, column=0, pady=5)
        self.departure_var = tk.StringVar()
        departure_combobox = ttk.Combobox(self.main_frame, textvariable=self.departure_var)
        departure_combobox['values'] = departure_airports
        departure_combobox.bind('<<ComboboxSelected>>', self.check_airport_selection)
        departure_combobox.grid(row=2, column=1, pady=5)

        # Show only Arrival Airport that exist in the database
        arrival_label = tk.Label(self.main_frame, text="Arrival airport")
        arrival_label.grid(row=3, column=0, pady=5)
        self.arrival_var = tk.StringVar()
        arrival_combobox = ttk.Combobox(self.main_frame, textvariable=self.arrival_var)
        arrival_combobox['values'] = arrival_airports
        arrival_combobox.bind('<<ComboboxSelected>>', self.check_airport_selection)
        arrival_combobox.grid(row=3, column=1, pady=5)

        # Étiquette pour afficher les messages d'erreur
        self.error_label = tk.Label(self.main_frame, text="", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Flight Research", command=self.redirect_to_Flight_booking)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        image_path = "../Pictures/avionResa.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(2)
        image_label = Label(self.main_frame, image=self.image)
        image_label.grid(row=0, column=2, rowspan=7, padx=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        cursor.close()
        conn.close()

    def check_airport_selection(self, event):
        if self.departure_var.get() == self.arrival_var.get():
            self.error_label.config(text="You can't have the same Departure Airport and Arrival Airport")
            self.search_button['state'] = 'disabled'
        else:
            self.error_label.config(text="")
            self.search_button['state'] = 'normal'

    def search_flights(self):
        date = self.date_var.get()
        departure = self.departure_var.get()
        arrival = self.arrival_var.get()
        person_type = self.person_type_var.get()
        print(f"Date: {date}, Départ: {departure}, Arrivée: {arrival}, Type de Personne: {person_type}")

    def redirect_to_Flight_booking(self):
        try:
            config.departure_airport = self.departure_var.get()
            config.arrival_airport = self.arrival_var.get()

            self.flightBooking_window = tk.Toplevel(self.root)
            self.app = FlightBooking.FlightSelectionPage(self.flightBooking_window, config.departure_airport, config.arrival_airport)
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()
