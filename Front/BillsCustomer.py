import tkinter as tk
from tkinter import ttk

class BillsHistory:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Page")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Invoice Page", font=("Helvetica", 16), pady=10)
        title_label.pack()

        invoice_list = ttk.Treeview(self.root, columns=("Date", "Flight", "Amount Paid"), show="headings", selectmode="browse")

        invoice_list.heading("Date", text="Date")
        invoice_list.column("Date", width=100)

        invoice_list.heading("Flight", text="Flight")
        invoice_list.column("Flight", width=150)

        invoice_list.heading("Amount Paid", text="Amount Paid")
        invoice_list.column("Amount Paid", width=100)

        self.add_dummy_data(invoice_list)

        invoice_list.pack(pady=20)
        invoice_list.bind("<ButtonRelease-1>", lambda event: self.show_invoice_details(invoice_list))

    def add_dummy_data(self, treeview):
        data = [
            ("2023-01-01", "Flight 123", "$500"),
            ("2023-02-15", "Flight 456", "$750"),
            ("2023-03-20", "Flight 789", "$1000"),
        ]

        for row in data:
            treeview.insert("", "end", values=row)

    def show_invoice_details(self, treeview):
        selected_item = treeview.selection()

        if selected_item:
            values = treeview.item(selected_item, "values")
            self.show_details_window(values)

    def show_details_window(self, invoice_info):
        details_window = tk.Toplevel(self.root)
        details_window.title("Invoice Details")

        flight_label = tk.Label(details_window, text=f"Flight: {invoice_info[1]}", font=("Helvetica", 12))
        flight_label.pack()

        date_label = tk.Label(details_window, text=f"Date: {invoice_info[0]}", font=("Helvetica", 12))
        date_label.pack()

        amount_label = tk.Label(details_window, text=f"Amount Paid: {invoice_info[2]}", font=("Helvetica", 12))
        amount_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BillsHistory(root)
    root.mainloop()
