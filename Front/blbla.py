import tkinter as tk

class FlightSelectionPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR FLY: Flight Booking")


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
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Crée un cadre pour le contenu de la page
        content_frame = tk.Frame(frame, bg="lightblue")
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.create_header(content_frame)
        self.create_flight_list(content_frame)

        # Configure le canvas pour ajuster automatiquement sa taille en fonction du contenu
        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_header(self, frame):
        header_label = tk.Label(frame, text="Select your flight", font=("Arial", 16, "bold"), bg="lightblue")
        header_label.pack(pady=20)

    def create_flight_list(self, frame):
        # Exemple de données de vol
        flight_data = [
            {"flight_number": "AE101", "departure": "New York", "arrival": "Los Angeles", "departure_time": "08:00 AM"},
            {"flight_number": "AE202", "departure": "Chicago", "arrival": "San Francisco", "departure_time": "09:30 AM"},
            {"flight_number": "AE303", "departure": "Miami", "arrival": "Houston", "departure_time": "11:15 AM"},
            # Ajoutez plus de données de vol ici
        ]

        for flight in flight_data:
            flight_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
            flight_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            flight_label = tk.Label(flight_frame, text=f"Flight {flight['flight_number']}", font=("Arial", 14, "bold"), bg="lightblue")
            flight_label.pack()

            departure_label = tk.Label(flight_frame, text=f"Departure: {flight['departure']}", font=("Arial", 12), bg="lightblue")
            departure_label.pack()

            arrival_label = tk.Label(flight_frame, text=f"Arrival: {flight['arrival']}", font=("Arial", 12), bg="lightblue")
            arrival_label.pack()

            departure_time_label = tk.Label(flight_frame, text=f"Departure time: {flight['departure_time']}", font=("Arial", 12), bg="lightblue")
            departure_time_label.pack()

            image_path = "../Pictures/avionResa.png"
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(3)

            image_label = tk.Label(flight_frame, image=image, bg="lightblue")
            image_label.image = image
            image_label.pack(side=tk.RIGHT, padx=10)

            reserve_button = tk.Button(flight_frame, text="Book", command=lambda f=flight: self.reserve_flight(f), bg="lightblue")
            reserve_button.pack(pady=10)

    def reserve_flight(self, selected_flight):
        print(f"Selected Flight: Flight {selected_flight['flight_number']}, Departure: {selected_flight['departure']}, Arrival: {selected_flight['arrival']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightSelectionPage(root)
    root.mainloop()