import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, ttk, messagebox
import subprocess
import platform
from PIL import Image, ImageTk

import config

class BookingApp:
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

        #background picture
        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)
        self.main_frame = tk.Frame(self.root, relief="solid", borderwidth=2)
        self.main_frame.grid(row=1, column=0, padx=15, pady=15)

        # logo picture
        image_path2 = "../Pictures/AirFly.png"
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

        departure_label = tk.Label(self.main_frame, text="Departure airport")
        departure_label.grid(row=2, column=0, pady=5)
        self.departure_var = tk.StringVar()
        departure_combobox = ttk.Combobox(self.main_frame, textvariable=self.departure_var)
        departure_combobox['values'] = ["Londres", "Paris", "New York"]
        departure_combobox.grid(row=2, column=1, pady=5)

        arrival_label = tk.Label(self.main_frame, text="Arrival airport")
        arrival_label.grid(row=3, column=0, pady=5)
        self.arrival_var = tk.StringVar()
        arrival_combobox = ttk.Combobox(self.main_frame, textvariable=self.arrival_var)
        arrival_combobox['values'] = ["Berlin", "Amsterdam", "Mexico"]
        arrival_combobox.grid(row=3, column=1, pady=5)


        search_button = tk.Button(self.main_frame, text="Flight Research", command=self.redirect_to_Flight_booking)
        search_button.grid(row=6, column=0, columnspan=2, pady=10)

        image_path = "../Pictures/avionResa.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(2)
        image_label = Label(self.main_frame, image=self.image)
        image_label.grid(row=0, column=2, rowspan=7, padx=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def search_flights(self):
        date = self.date_var.get()
        departure = self.departure_var.get()
        arrival = self.arrival_var.get()
        person_type = self.person_type_var.get()
        print(f"Date: {date}, Départ: {departure}, Arrivée: {arrival}, Type de Personne: {person_type}")

    def redirect_to_Flight_booking(self):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "FlightBooking.py"], shell=True)
            else:
                subprocess.Popen(["python3", "FlightBooking.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()
