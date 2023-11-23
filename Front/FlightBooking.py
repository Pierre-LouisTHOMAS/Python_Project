import tkinter as tk
from tkinter import ttk
import pymysql
import config
import BookFlight
from datetime import datetime
import random
from decimal import Decimal



class FlightSelectionPage:
    def __init__(self, root, departure_date, departure_airport, arrival_airport, num_tickets):
        self.root = root
        self.date_flight = departure_date
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.num_tickets = num_tickets
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Flight Research Result")

        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        canvas = tk.Canvas(root)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)


        frame = tk.Frame(canvas, bg="lightblue")
        #canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.create_window((0, 0), window=frame, anchor="nw", width=root.winfo_screenwidth())

        content_frame = tk.Frame(frame, bg="lightblue")
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.create_header(content_frame)
        self.create_flight_list(content_frame)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def redirect_to_home_page(self, event):
            self.root.destroy()

    def create_header(self, frame):
        header_label = tk.Label(frame, text="Select your flight", font=("Arial", 18, "bold italic"), bg="lightblue")
        header_label.pack(pady=20)

        # logo picture
        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(8)
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


        query = "SELECT Flight_ID, Departure_Date, Arrival_Date, Departure_Airport, Arrival_Airport, Price FROM Flight"

        where_conditions = []
        params = []

        if config.departure_date:
            config.departure_date = datetime.strptime(config.departure_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            where_conditions.append("DATE(Departure_Date) = %s")
            params.append(config.departure_date)
        if config.departure_airport:
            where_conditions.append("Departure_Airport = %s")
            params.append(config.departure_airport)
        if config.arrival_airport:
            where_conditions.append("Arrival_Airport = %s")
            params.append(config.arrival_airport)

        if where_conditions:
            query += " WHERE " + " AND ".join(where_conditions)

        cursor.execute(query, params)

        flight_data = cursor.fetchall()

        for flight in flight_data:
            # Create a white band between each flight frame
            white_band = tk.Frame(frame, height=25, bg="white")
            white_band.pack(fill=tk.X)

            flight_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
            flight_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)

            departure_date_label = tk.Label(flight_frame, text=f"{flight['Departure_Date']}",
                                            font=("Arial", 14, "bold"), bg="lightblue")
            departure_date_label.grid(row=0, column=0, padx=(30, 40), pady=15, sticky="w")

            departure_airport_label = tk.Label(flight_frame, text=f"{flight['Departure_Airport']}",
                                               font=("Arial", 11), bg="lightblue")
            departure_airport_label.grid(row=1, column=0, padx=(60, 40), pady=10, sticky="w")

            arrow_canvas = tk.Canvas(flight_frame, width=20, height=40, bg="lightblue", highlightthickness=0)
            arrow_canvas.grid(row=0, column=0, rowspan=2, padx=(10, 0), pady=5, sticky="e")
            arrow_canvas.create_line(0, 30, 20, 30, arrow=tk.LAST)

            arrival_date_label = tk.Label(flight_frame, text=f"{flight['Arrival_Date']}",
                                          font=("Arial", 14, "bold"), bg="lightblue")
            arrival_date_label.grid(row=0, column=1, padx=(30, 40), pady=15, sticky="w")

            arrival_airport_label = tk.Label(flight_frame, text=f"{flight['Arrival_Airport']}",
                                             font=("Arial", 11), bg="lightblue")
            arrival_airport_label.grid(row=1, column=1, padx=(60, 40), pady=10, sticky="w")

            separator1 = ttk.Separator(flight_frame, orient="vertical")
            separator1.grid(row=0, column=2, rowspan=2, padx=10, sticky="ns")

            random_number_of_tickets = random.randint(1, 300)

            number_ticket = tk.Label(flight_frame, text=f"Number of Tickets: {random_number_of_tickets}",
                                     font=("Arial", 11), bg="lightblue")
            number_ticket.grid(row=0, column=3, padx=(60, 40), pady=10, sticky="w")

            separator2 = ttk.Separator(flight_frame, orient="vertical")
            separator2.grid(row=0, column=4, rowspan=2, padx=10, sticky="ns")


            if config.user_discount is None:
                config.user_discount = Decimal(0)
            else:
                discount_factor = Decimal(config.user_discount) / Decimal(100)
                total_price = flight['Price'] * Decimal(self.num_tickets) * (Decimal(1) - discount_factor)

            price_label2 = tk.Label(flight_frame, text=f"Economy ticket : {total_price:.2f}", font=("Arial", 12), bg="lightblue")
            price_label2.grid(row=0, column=5, padx=(20, 40), pady=15, sticky="w")


            reserve_button2 = tk.Button(flight_frame, text="Book", command=lambda f=flight: self.update_and_redirect(f),
                                        bg="lightblue")
            reserve_button2.grid(row=1, column=5, padx=(30, 40), pady=10, sticky="n")

            if config.user_type == 'Employee':
                modify_button = tk.Button(flight_frame, text="Modify", command=lambda f=flight: self.modify_flight(f),
                                          bg="red")
                modify_button.grid(row=1, column=7, padx=(30, 40), pady=10, sticky="n")
            else:
                image_path = "../Pictures/avionResa.png"
                image = tk.PhotoImage(file=image_path)
                image = image.subsample(4)

                image_label = tk.Label(flight_frame, image=image, bg="lightblue")
                image_label.image = image
                image_label.grid(row=0, column=7, rowspan=2, padx=(1, 40), pady=15, sticky="e")

        cursor.close()
        conn.close()

    def modify_flight(self, flight):
        print(f"Modify Flight: {flight}")
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

    def reserve_flight(self, selected_flight):
        print(f"Selected Flight: Flight {selected_flight['flight_number']}, Departure: {selected_flight['departure']}, Arrival: {selected_flight['arrival']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightSelectionPage(root)
    root.mainloop()