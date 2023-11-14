import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, ttk
from PIL import Image, ImageTk

import pymysql
import config

class BookFlight:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND: Book Page")

        self.header_height = root.winfo_screenheight() * 0.22
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.menu = None

        self.create_window()


    def redirect_to_flightBooking_page(self, event):
        self.root.destroy()
    def create_window(self):
        self.background_image = Image.open("../Pictures/Boreale.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2, bg="white")
        image_label2.place(x=self.header_height * 6.5, y=self.header_height * 0.1)
        # Return to FlightBooking.py page
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_flightBooking_page(event))

        frame_width = 400
        frame_height = 250
        white_frame = tk.Frame(self.root, bg="white", width=frame_width, height=frame_height)
        white_frame.place(relx=0.5, rely=0.5, anchor='center')

        flight_info_label = tk.Label(white_frame, text="Flight Information", font=("Helvetica", 16), bg="white")
        flight_info_label.pack(pady=20)

        departure_airport = config.selected_departure_airport
        arrival_airport = config.selected_arrival_airport
        departure_time = config.selected_departure_date
        arrival_time = config.selected_arrival_date
        price = config.selected_price

        labels_frame = tk.Frame(white_frame, bg="white")
        labels_frame.pack()


        departure_label = tk.Label(labels_frame, text=f"Departure: {departure_airport}", bg="white", font=("Helvetica", 12))
        departure_label.pack(pady=5)

        arrival_label = tk.Label(labels_frame, text=f"Arrival: {arrival_airport}", bg="white", font=("Helvetica", 12))
        arrival_label.pack(pady=5)

        departure_time_label = tk.Label(labels_frame, text=f"Departure Time: {departure_time}", bg="white", font=("Helvetica", 12))
        departure_time_label.pack(pady=5)

        arrival_time_label = tk.Label(labels_frame, text=f"Arrival Time: {arrival_time}", bg="white", font=("Helvetica", 12))
        arrival_time_label.pack(pady=5)

        price_label = tk.Label(white_frame, text=f"Price: {price}", bg="white", font=("Helvetica", 14, "bold"))
        price_label.pack(pady=10)

        pay_button = tk.Button(white_frame, text="Pay", command=self.pay, font=("Helvetica", 12, "bold"), bg='white', fg='black')
        pay_button.pack(pady=10)

    def pay(self):
        # Add payment logic here
        print("Payment button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookFlight(root)
    root.mainloop()
