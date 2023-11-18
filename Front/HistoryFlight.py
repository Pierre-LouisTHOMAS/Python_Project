import tkinter as tk
from tkinter import ttk

class ReservationHistory:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation History")

        self.create_information()

    def create_information(self):

        title_label = tk.Label(self.root, text="Reservation History", font=("Helvetica", 16), pady=10)
        title_label.pack()

        reservation_list = ttk.Treeview(self.root, columns=("Date", "Flight", "Status"), show="headings", selectmode="browse")

        reservation_list.heading("Date", text="Date")
        reservation_list.column("Date", width=100)

        reservation_list.heading("Flight", text="Flight")
        reservation_list.column("Flight", width=150)

        reservation_list.heading("Status", text="Status")
        reservation_list.column("Status", width=100)

        self.add_dummy_data(reservation_list)

        reservation_list.pack(pady=20)

        reservation_list.bind("<ButtonRelease-1>", lambda event: self.show_reservation_details(reservation_list))

    def add_dummy_data(self, treeview):
        data = [
            ("2023-01-01", "Flight 123", "Confirmed"),
            ("2023-02-15", "Flight 456", "Cancelled"),
            ("2023-03-20", "Flight 789", "Pending"),
        ]

        for row in data:
            treeview.insert("", "end", values=row)

    def show_reservation_details(self, treeview):

        selected_item = treeview.selection()

        if selected_item:
            values = treeview.item(selected_item, "values")
            self.show_details_window(values)

    def show_details_window(self, reservation_info):
        details_window = tk.Toplevel(self.root)
        details_window.title("Reservation Details")

        flight_label = tk.Label(details_window, text=f"Flight: {reservation_info[1]}", font=("Helvetica", 12))
        flight_label.pack()

        date_label = tk.Label(details_window, text=f"Date: {reservation_info[0]}", font=("Helvetica", 12))
        date_label.pack()

        status_label = tk.Label(details_window, text=f"Status: {reservation_info[2]}", font=("Helvetica", 12))
        status_label.pack()

        customer_name_label = tk.Label(details_window, text="Customer: John Doe", font=("Helvetica", 12))
        customer_name_label.pack()

        customer_email_label = tk.Label(details_window, text="Email: john.doe@example.com", font=("Helvetica", 12))
        customer_email_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationHistory(root)
    root.mainloop()
