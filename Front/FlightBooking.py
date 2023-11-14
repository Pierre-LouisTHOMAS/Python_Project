import tkinter as tk
import subprocess
import platform
from tkinter import Toplevel, messagebox, ttk
import pymysql
import config
import BookFlight

class FlightSelectionPage:
    def __init__(self, root, departure_airport, arrival_airport):
        self.root = root
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR FLY: Flight Booking")

        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        # Crée un canvas pour contenir la barre de défilement et un cadre intermédiaire
        canvas = tk.Canvas(root)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crée une barre de défilement
        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure le canvas pour utiliser la barre de défilement
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crée un cadre à l'intérieur du canvas
        frame = tk.Frame(canvas, bg="lightblue")
        #canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.create_window((0, 0), window=frame, anchor="nw", width=root.winfo_screenwidth())


        # Crée un cadre pour le contenu de la page
        content_frame = tk.Frame(frame, bg="lightblue")
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.create_header(content_frame)
        self.create_flight_list(content_frame)

        # Configure le canvas pour ajuster automatiquement sa taille en fonction du contenu
        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def redirect_to_home_page(self, event):
            self.root.destroy()

    def create_header(self, frame):
        header_label = tk.Label(frame, text="Select your flight", font=("Arial", 16, "bold"), bg="lightblue")
        header_label.pack(pady=20)

        # logo picture
        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.header_height * 0.7, y=self.header_height * 0.1)

        # Return to home page
        image_label2.bind("<Button-1>", self.redirect_to_home_page)

    def create_flight_list(self, frame):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # Commencez par la requête de base
        query = "SELECT Flight_ID, Departure_Date, Arrival_Date, Departure_Airport, Arrival_Airport, Price FROM Flight"

        # Créez une liste pour les conditions WHERE et une autre pour les paramètres
        where_conditions = []
        params = []

        # Ajoutez des conditions si des aéroports sont spécifiés
        if config.departure_airport:
            where_conditions.append("Departure_Airport = %s")
            params.append(config.departure_airport)
        if config.arrival_airport:
            where_conditions.append("Arrival_Airport = %s")
            params.append(config.arrival_airport)

        # Si des conditions WHERE existent, ajoutez-les à la requête
        if where_conditions:
            query += " WHERE " + " AND ".join(where_conditions)

        # Exécutez la requête avec les paramètres
        cursor.execute(query, params)

        # import the database is flight_data
        flight_data = cursor.fetchall()

        for flight in flight_data:
            flight_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
            flight_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            flight_label = tk.Label(flight_frame, text=f"Flight number {flight['Flight_ID']}", font=("Arial", 14, "bold"), bg="lightblue")
            flight_label.pack()

            departure_label = tk.Label(flight_frame, text=f"Departure date: {flight['Departure_Date']}", font=("Arial", 12),bg="lightblue")
            departure_label.pack()

            arrival_label = tk.Label(flight_frame, text=f"Arrival date: {flight['Arrival_Date']}", font=("Arial", 12), bg="lightblue")
            arrival_label.pack()

            departure_label = tk.Label(flight_frame, text=f"Departure airport: {flight['Departure_Airport']}", font=("Arial", 12), bg="lightblue")
            departure_label.pack()

            arrival_label = tk.Label(flight_frame, text=f"Arrival airport: {flight['Arrival_Airport']}", font=("Arial", 12),bg="lightblue")
            arrival_label.pack()

            departure_time_label = tk.Label(flight_frame, text=f"Price: {flight['Price']}",font=("Arial", 12), bg="lightblue")
            departure_time_label.pack()

            image_path = "../Pictures/avionResa.png"
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(3)

            image_label = tk.Label(flight_frame, image=image, bg="lightblue")
            image_label.image = image
            image_label.pack(side=tk.RIGHT, padx=10)

            reserve_button = tk.Button(flight_frame, text="Book", command=lambda f=flight: self.update_and_redirect(f), bg="lightblue")
            reserve_button.pack(pady=10)

        cursor.close()
        conn.close()

    def update_and_redirect(self, flight):
        config.selected_flight_id = flight['Flight_ID']
        config.selected_departure_date = flight['Departure_Date']
        config.selected_arrival_date = flight['Arrival_Date']
        config.selected_departure_airport = flight['Departure_Airport']
        config.selected_arrival_airport = flight['Arrival_Airport']
        config.selected_price = flight['Price']

        self.redirect_to_book_flight()

    def redirect_to_book_flight(self):
        self.bookFlight_window = tk.Toplevel(self.root)
        self.app = BookFlight.BookFlight(self.bookFlight_window)

    #for flight in flight_data:
        #    flight_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
        #    flight_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        #
        #    flight_label = tk.Label(flight_frame, text=f"Flight {flight['flight_number']}", font=("Arial", 14, "bold"), bg="lightblue")
        #    flight_label.pack()
        #
        #    departure_label = tk.Label(flight_frame, text=f"Departure: {flight['departure']}", font=("Arial", 12), bg="lightblue")
        #    departure_label.pack()
        #
        #    arrival_label = tk.Label(flight_frame, text=f"Arrival: {flight['arrival']}", font=("Arial", 12), bg="lightblue")
        #    arrival_label.pack()
        #
        #    departure_time_label = tk.Label(flight_frame, text=f"Departure time: {flight['departure_time']}", font=("Arial", 12), bg="lightblue")
        #    departure_time_label.pack()
        #
        #    image_path = "../Pictures/avionResa.png"
        #    image = tk.PhotoImage(file=image_path)
        #    image = image.subsample(3)
        #
        #    image_label = tk.Label(flight_frame, image=image, bg="lightblue")
        #    image_label.image = image
        #    image_label.pack(side=tk.RIGHT, padx=10)
        #
        #    reserve_button = tk.Button(flight_frame, text="Book", command=lambda f=flight: self.reserve_flight(f), bg="lightblue")
        #    reserve_button.pack(pady=10)

    def reserve_flight(self, selected_flight):
        print(f"Selected Flight: Flight {selected_flight['flight_number']}, Departure: {selected_flight['departure']}, Arrival: {selected_flight['arrival']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightSelectionPage(root)
    root.mainloop()