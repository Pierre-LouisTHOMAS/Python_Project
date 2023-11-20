import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Toplevel, messagebox, ttk
import AccountInformation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import FlightBooking
import UserInfo
import pymysql
import config


class HomeEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Employee Page")

        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        self.header_height = root.winfo_screenheight() * 0.22
        self.menu = None

        self.create_header()

    def redirect_to_home_page(self, event):
        self.root.destroy()

    def create_header(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        title_label = tk.Label(self.root, text="Employee home page",font=("Arial", 20, "bold italic"), bg="white")
        title_label.place(x=self.window_width * 0.43, y=self.window_height * 0.07)

        image_path = "../Pictures/barre_recherche.png"
        self.image_button = tk.PhotoImage(file=image_path)
        image_button_label = tk.Label(self.root, image=self.image_button, cursor="hand2", bg="white")
        image_button_label.place(x=self.window_width * 0.01, y=self.window_height * 0.06)
        image_button_label.bind("<Button-1>", self.create_menu)

        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(7)
        image_label2 = tk.Label(self.root, image=self.image2, bg="white")
        image_label2.place(x=self.window_width * 0.3, y=self.window_height * 0.03)
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))


        image_path4 = "../Pictures/AccountPicture.png"
        self.image4 = tk.PhotoImage(file=image_path4)
        self.image4 = self.image4.subsample(6)
        image_label4 = tk.Label(self.root, image=self.image4, bg="white")
        image_label4.place(x=self.window_width * 0.93, y=self.window_height * 0.04)
        image_label4.bind("<Button-1>", self.redirect_to_account_information)

        image_path3 = "../Pictures/bg4.png"
        self.image3 = tk.PhotoImage(file=image_path3)
        image_label3 = tk.Label(self.root, image=self.image3, bg="white")
        image_label3.place(x=0, y=self.window_height * 0.2, relwidth=1)

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

            #under Menu name
            flight_menu.add_command(label="flight available", command=self.window_flight_available)
            flight_menu.add_command(label="flight discount offer", command=self.save)
            customer_menu.add_command(label="Customer file management", command=self.window_file_management)
            customer_menu.add_command(label="Customer reservation history", command=self.window_history_reservation)
            customer_menu.add_command(label="number of tickets purchased", command=self.window_history_reservation)
            sale_menu.add_command(label="Sales analysis", command=self.sales_analysis)
            sale_menu.add_command(label="Amount of private flight sale", command=self.save)

            #Menu name
            self.menu.add_cascade(label="Flight", menu=flight_menu)
            self.menu.add_cascade(label="Customer", menu=customer_menu)
            self.menu.add_cascade(label="Sale", menu=sale_menu)
            self.menu.post(x, y)


    def window_file_management(self):
        user_info_window = tk.Toplevel(self.root)
        user_info_window.title("User Information")
        user_info_window.geometry("300x200")
        user_info_window.configure(bg="white")
        self.main_frame = tk.Frame(user_info_window, relief="solid", borderwidth=2)
        self.main_frame.pack(padx=10, pady=10)


        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT DISTINCT Email FROM User WHERE Type='Member'")
        email_info = [info['Email'] for info in cursor.fetchall()]

        email_label = tk.Label(self.main_frame, text="Email")
        email_label.grid(row=2, column=0, pady=5)
        self.email_var = tk.StringVar()
        email_combobox = ttk.Combobox(self.main_frame, textvariable=self.email_var)
        email_combobox['values'] = email_info
        email_combobox.bind('<<ComboboxSelected>>')
        email_combobox.grid(row=2, column=1, pady=5)

        self.submit_button = tk.Button(self.main_frame, text="Research", command=self.redirect_to_user_info)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        cursor.close()
        conn.close()


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

        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT DISTINCT Departure_Airport FROM Flight")
        departure_airports = [airport['Departure_Airport'] for airport in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT Arrival_Airport FROM Flight")
        arrival_airports = [airport['Arrival_Airport'] for airport in cursor.fetchall()]

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
        departure_combobox['values'] = departure_airports
        departure_combobox.bind('<<ComboboxSelected>>', self.check_airport_selection)
        departure_combobox.grid(row=2, column=1, pady=5)

        arrival_label = tk.Label(self.main_frame, text="Arrival airport")
        arrival_label.grid(row=3, column=0, pady=5)
        self.arrival_var = tk.StringVar()
        arrival_combobox = ttk.Combobox(self.main_frame, textvariable=self.arrival_var)
        arrival_combobox['values'] = arrival_airports
        arrival_combobox.bind('<<ComboboxSelected>>', self.check_airport_selection)
        arrival_combobox.grid(row=3, column=1, pady=5)

        self.error_label = tk.Label(self.main_frame, text="", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, pady=5)
        self.submit_button = tk.Button(self.main_frame, text="Research", command=self.redirect_to_edit_flight)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        cursor.close()
        conn.close()

    def check_airport_selection(self, event):
        if self.departure_var.get() == self.arrival_var.get():
            self.error_label.config(text="You can't have the same Departure Airport and Arrival Airport")
            self.submit_button['state'] = 'disabled'
        else:
            self.error_label.config(text="")
            self.submit_button['state'] = 'normal'

    def sales_analysis(self):
        # Remplacer Label et Value par les valeurs de la BDD
        labels = ['London', 'Paris', 'Mexico', 'Berlin', 'Tokyo']
        values = [25, 40, 35, 5, 10]

        plt.bar(labels, values)
        plt.xlabel("City")
        plt.ylabel("Number of flights")
        plt.title("Flight analysis")
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Flight analysis Graph")

        canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        graph_window.mainloop()

    def redirect_to_account_information(self, event):
        self.accountPage_window = tk.Toplevel(self.root)
        self.app = AccountInformation.EmployeeAccount(self.accountPage_window)

    def redirect_to_edit_flight(self):
        try:
            config.departure_airport = self.departure_var.get()
            config.arrival_airport = self.arrival_var.get()

            self.editFlight_window = tk.Toplevel(self.root)
            self.app = FlightBooking.FlightSelectionPage(self.editFlight_window,config.departure_airport, config.arrival_airport)

        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")


    def redirect_to_user_info(self):
        try:
            config.email_info = self.email_var.get()

            self.user_info_window = tk.Toplevel(self.root)
            self.app = UserInfo.UserInfoPage(self.user_info_window,config.email_info)

        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection bbb{e}")

    def save(self):
        print("Vous avez enregistré")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeEmployee(root)
    root.mainloop()
