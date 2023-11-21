import tkinter as tk
from tkinter import ttk
import pymysql

import config

class ReservationHistory:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation History")

        self.create_information()

    def create_information(self):

        title_label = tk.Label(self.root, text="Reservation History", font=("Helvetica", 16), pady=10)
        title_label.pack()

        reservation_list = ttk.Treeview(self.root, columns=("Date", "Departure_Airport", "Arrival_Airport"), show="headings", selectmode="browse")

        reservation_list.heading("Date", text="Date")
        reservation_list.column("Date", width=100)

        reservation_list.heading("Departure_Airport", text="Departure Airport")
        reservation_list.column("Departure_Airport", width=150)

        reservation_list.heading("Arrival_Airport", text="Arrival Airport")
        reservation_list.column("Arrival_Airport", width=100)

        self.add_dummy_data(reservation_list)

        reservation_list.pack(pady=20)

        reservation_list.bind("<ButtonRelease-1>", lambda event: self.show_reservation_details(reservation_list))

    def add_dummy_data(self, treeview):
        user_id = config.user_id

        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='AirlineDatabase',
                port=8889
            )
            cursor = conn.cursor()

            query = """
                    SELECT f.Departure_Date, f.Departure_Airport, f.Arrival_Airport, u.First_Name, u.Email 
                    FROM Reservation r 
                    JOIN Flight f ON r.Flight_ID = f.Flight_ID 
                    JOIN User u ON r.User_ID = u.User_ID 
                    WHERE r.User_ID = %s
                    """
            cursor.execute(query, (user_id,))

            reservations = cursor.fetchall()

            for reservation in reservations:
                treeview.insert("", "end", values=reservation)

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()

    def show_reservation_details(self, treeview):

        selected_item = treeview.selection()

        if selected_item:
            values = treeview.item(selected_item, "values")
            self.show_details_window(values)

    def show_details_window(self, reservation_info):
        details_window = tk.Toplevel(self.root)
        details_window.title("Reservation Details")

        # Assurez-vous que l'indexation correspond à l'ordre des données dans le treeview
        date_label = tk.Label(details_window, text=f"Date: {reservation_info[0]}", font=("Helvetica", 12))
        date_label.pack()

        departure_airport_label = tk.Label(details_window, text=f"Departure Airport: {reservation_info[1]}",
                                           font=("Helvetica", 12))
        departure_airport_label.pack()

        arrival_airport_label = tk.Label(details_window, text=f"Arrival Airport: {reservation_info[2]}",
                                         font=("Helvetica", 12))
        arrival_airport_label.pack()

        customer_name_label = tk.Label(details_window, text=f"Customer: {reservation_info[3]}", font=("Helvetica", 12))
        customer_name_label.pack()

        customer_email_label = tk.Label(details_window, text=f"Email: {reservation_info[4]}", font=("Helvetica", 12))
        customer_email_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationHistory(root)
    root.mainloop()
