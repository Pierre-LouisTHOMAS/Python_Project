import tkinter as tk

class FlightSelectionPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR FLY: Flight Booking")

        # Crée un cadre pour le header
        header_frame = tk.Frame(self.root, bg="lightblue")
        header_frame.pack(fill=tk.X)

        self.create_header(header_frame)
        self.create_flight_list()


    def create_header(self,header_frame):
        header_label = tk.Label(self.root, text="Select your flight", font=("Arial", 16, "bold"))
        header_label.pack(pady=20)



    def create_flight_list(self):
        # Exemple de vol
        flight_data = [
            {"flight_number": "AE101", "departure": "New York", "arrival": "Los Angeles", "departure_time": "08:00 AM", "arrival_time": "11:00 AM"},
            {"flight_number": "AE202", "departure": "Chicago", "arrival": "San Francisco", "departure_time": "09:30 AM", "arrival_time": "01:00 PM"},
            {"flight_number": "AE303", "departure": "Miami", "arrival": "Houston", "departure_time": "11:15 AM", "arrival_time": "10:30 AM"},

        ]

        for flight in flight_data:
            flight_frame = tk.Frame(self.root, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
            flight_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

            flight_label = tk.Label(flight_frame, text=f"Flight {flight['flight_number']}", font=("Arial", 14, "bold"), bg="lightblue")
            flight_label.pack()

            departure_label = tk.Label(flight_frame, text=f"Departure: {flight['departure']}", font=("Arial", 12), bg="lightblue")
            departure_label.pack()

            arrival_label = tk.Label(flight_frame, text=f"Arrival: {flight['arrival']}", font=("Arial", 12), bg="lightblue")
            arrival_label.pack()

            departure_time_label = tk.Label(flight_frame, text=f"departure time: {flight['departure_time']}", font=("Arial", 12), bg="lightblue")
            departure_time_label.pack()

            arrival_time_label = tk.Label(flight_frame, text=f"arrival time: {flight['arrival_time']}",
                                            font=("Arial", 12), bg="lightblue")
            arrival_time_label.pack()

            image_path = "../Pictures/avionResa.png"
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(3)

            image_label = tk.Label(flight_frame, image=image, bg="lightblue")
            image_label.image = image
            image_label.pack(side=tk.RIGHT, padx=10)


            button_frame = tk.Frame(flight_frame, bg="lightblue")
            button_frame.pack(expand=True)

            reserve_button = tk.Button(button_frame, text="Book", command=lambda f=flight: self.reserve_flight(f), bg="lightblue")
            reserve_button.pack(side=tk.RIGHT)

    def reserve_flight(self, selected_flight):
        print(f"Vol sélectionné : Vol {selected_flight['flight_number']}, Départ : {selected_flight['departure']}, Arrivée : {selected_flight['arrival']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightSelectionPage(root)
    root.mainloop()
