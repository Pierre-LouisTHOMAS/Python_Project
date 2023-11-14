import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, ttk
from tkinter import Toplevel, messagebox, ttk
import subprocess
import platform

class HomeEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND: Home Page")

        self.header_height = root.winfo_screenheight() * 0.22
        self.menu = None

        self.create_header()

    def redirect_to_home_page(self, event):
        self.root.destroy()  # Ferme uniquement la fenêtre de connection

    def create_header(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        title_label = tk.Label(self.root, text="Employee home page",font=("Arial", 20, "bold italic"), bg="white")
        title_label.place(x=self.header_height * 3.2, y=self.header_height * 0.4)

        image_path = "../Pictures/barre_recherche.png"
        self.image_button = tk.PhotoImage(file=image_path)
        image_button_label = tk.Label(self.root, image=self.image_button, cursor="hand2", bg="white")
        image_button_label.place(x=self.header_height * 0.2, y=self.header_height * 0.3)
        image_button_label.bind("<Button-1>", self.create_menu)

        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2, bg="white")
        image_label2.place(x=self.header_height * 2.5, y=self.header_height * 0.2)
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))

        image_path4 = "../Pictures/AccountPicture.png"
        self.image4 = tk.PhotoImage(file=image_path4)
        self.image4 = self.image4.subsample(6)
        image_label4 = tk.Label(self.root, image=self.image4, bg="white")
        image_label4.place(x=self.header_height * 7.4, y=self.header_height * 0.3)
        image_label4.bind("<Button-1>", self.redirect_to_open_account)

        image_path3 = "../Pictures/Boreale.png"
        self.image3 = tk.PhotoImage(file=image_path3)
        image_label3 = tk.Label(self.root, image=self.image3, bg="white")
        image_label3.place(x=0, y=self.header_height * 1.05, relwidth=1, relheight=0.75)

    def create_menu(self, event):
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None
        else:

            image_button_label = event.widget
            x, y = image_button_label.winfo_rootx(), image_button_label.winfo_rooty()
            self.menu = tk.Menu(self.root, tearoff=0)

            flight_menu = tk.Menu(self.menu, tearoff=0)
            customer_menu = tk.Menu(self.menu, tearoff=0)
            sale_menu = tk.Menu(self.menu, tearoff=0)


            flight_menu.add_command(label="flight available", command=self.window_flight_available)
            flight_menu.add_command(label="flight discount offer", command=self.save)
            customer_menu.add_command(label="Customer file management", command=self.window_file_management)
            customer_menu.add_command(label="Customer reservation history", command=self.window_history_reservation)
            customer_menu.add_command(label="number of tickets purchased", command=self.window_history_reservation)
            sale_menu.add_command(label="Sales analysis", command=self.save)
            sale_menu.add_command(label="Amount of private flight sale", command=self.save)
            self.menu.add_cascade(label="Flight", menu=flight_menu)
            self.menu.add_cascade(label="Customer", menu=customer_menu)
            self.menu.add_cascade(label="Sale", menu=sale_menu)
            self.menu.post(x, y)

    def window_file_management(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Customer file management")
        client_window.geometry("300x200")
        client_window.configure(bg="white")

        mail_label = tk.Label(client_window, text="Mail:")
        mail_label.pack()

        mail_entry = tk.Entry(client_window)
        mail_entry.pack()

        id_label = tk.Label(client_window, text="ID:")
        id_label.pack()

        id_entry = tk.Entry(client_window)
        id_entry.pack()

        submit_button = tk.Button(client_window, text="Submit", command=self.save)
        submit_button.pack()

    def window_history_reservation(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Customer reservation history")
        client_window.geometry("300x200")
        client_window.configure(bg="white")

        mail_label = tk.Label(client_window, text="Mail:")
        mail_label.pack()

        mail_entry = tk.Entry(client_window)
        mail_entry.pack()

        id_label = tk.Label(client_window, text="ID:")
        id_label.pack()

        id_entry = tk.Entry(client_window)
        id_entry.pack()

        submit_button = tk.Button(client_window, text="History", command=self.save)
        submit_button.pack()
        number_ticket = tk.Button(client_window, text="Number_ticket", command=self.save)
        number_ticket.pack()

    def window_flight_available(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Flight available")
        client_window.geometry("300x200")
        client_window.configure(bg="white")
        self.main_frame = tk.Frame(client_window, relief="solid", borderwidth=2)
        self.main_frame.pack(padx=10, pady=10)

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

        submit_button = tk.Button(self.main_frame, text="Research", command=self.save)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def redirect_to_open_account(self, event):
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "EmployeeAccount.py"], shell=True)
            else:
                subprocess.Popen(["python3", "EmployeeAccount.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")


    def save(self):
        print("Vous avez enregistré")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeEmployee(root)
    root.mainloop()
