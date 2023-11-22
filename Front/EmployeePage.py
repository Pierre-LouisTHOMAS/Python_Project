import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Toplevel, messagebox, ttk, Label
from PIL import Image, ImageTk
import AccountInformation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

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
        config.is_user_logged_in = False
        config.user_email = None
        config.user_id = None
        config.first_name_user = None
        config.last_name_user = None
        config.user_type = 0
        config.member_category = 0
        config.flight_data = []
        config.departure_date = None
        config.departure_airport = None
        config.arrival_airport = None
        config.selected_flight_id = None
        config.selected_departure_date = None
        config.selected_arrival_date = None
        config.selected_departure_airport = None
        config.selected_arrival_airport = None
        config.selected_price = None
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
            flight_menu.add_command(label="add new flight", command=self.add_flight_window)
            flight_menu.add_command(label="number of tickets purchased", command=self.window_flight_available)
            customer_menu.add_command(label="Customer file management", command=self.window_file_management)
            customer_menu.add_command(label="Customer reservation history", command=self.window_history_reservation)
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
        history_reservation_window = tk.Toplevel(self.root)
        history_reservation_window.title("Customer reservation history")
        history_reservation_window.geometry("300x200")
        history_reservation_window.configure(bg="white")
        self.main_frame = tk.Frame(history_reservation_window, relief="solid", borderwidth=2)
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

        self.submit_button = tk.Button(self.main_frame, text="Research", command=self.redirect_to_user_flight_history)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        cursor.close()
        conn.close()

    def window_flight_available(self):
        client_window = tk.Toplevel(self.root)
        client_window.title("Flight available")
        client_window.geometry("800x300")
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

        self.search_button = tk.Button(self.main_frame, text="Flight Research", command=self.redirect_to_Flight_booking)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        image_path = "../Pictures/avionResa.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(2)
        image_label = Label(self.main_frame, image=self.image)
        image_label.grid(row=0, column=2, rowspan=7, padx=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        cursor.close()
        conn.close()

    def check_airport_selection(self, event):
        if self.departure_var.get() == self.arrival_var.get():
            self.error_label.config(text="You can't have the same Departure Airport and Arrival Airport")
            self.search_button['state'] = 'disabled'
        else:
            self.error_label.config(text="")
            self.search_button['state'] = 'normal'
    def search_flights(self):
        date = self.date_var.get()
        departure = self.departure_var.get()
        arrival = self.arrival_var.get()
        person_type = self.person_type_var.get()
        print(f"Date: {date}, Départ: {departure}, Arrivée: {arrival}, Type de Personne: {person_type}")
    def redirect_to_Flight_booking(self):
        try:
            config.departure_date = self.date_var.get()
            config.departure_airport = self.departure_var.get()
            config.arrival_airport = self.arrival_var.get()

            self.flightBooking_window = tk.Toplevel(self.root)
            self.app = FlightBooking.FlightSelectionPage(self.flightBooking_window, config.departure_date, config.departure_airport, config.arrival_airport)
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def add_flight_window(self):
        add_flight_window = tk.Toplevel(self.root)
        add_flight_window.title("Add a new flight")
        add_flight_window.geometry("400x300")
        add_flight_window.configure(bg="white")
        main_frame = tk.Frame(add_flight_window, relief="solid", borderwidth=2)
        main_frame.pack(padx=10, pady=10)

        # Widgets pour la saisie des informations
        departure_label = tk.Label(main_frame, text="Departure airport")
        departure_label.grid(row=0, column=0, pady=5)
        departure_entry = tk.Entry(main_frame)
        departure_entry.grid(row=0, column=1, pady=5)

        arrival_label = tk.Label(main_frame, text="Arrival airport")
        arrival_label.grid(row=1, column=0, pady=5)
        arrival_entry = tk.Entry(main_frame)
        arrival_entry.grid(row=1, column=1, pady=5)

        departure_date_label = tk.Label(main_frame, text="Departure date")
        departure_date_label.grid(row=2, column=0, pady=5)
        departure_date_entry = DateEntry(main_frame, date_pattern="yyyy-mm-dd")
        departure_date_entry.grid(row=2, column=1, pady=5)

        arrival_date_label = tk.Label(main_frame, text="Arrival date")
        arrival_date_label.grid(row=3, column=0, pady=5)
        arrival_date_entry = DateEntry(main_frame, date_pattern="yyyy-mm-dd")
        arrival_date_entry.grid(row=3, column=1, pady=5)

        price_label = tk.Label(main_frame, text="Price")
        price_label.grid(row=4, column=0, pady=5)
        price_entry = tk.Entry(main_frame)
        price_entry.grid(row=4, column=1, pady=5)

        add_button = tk.Button(main_frame, text="Add a new flight", command=lambda: self.ajouter_vol(
            departure_entry.get(),
            arrival_entry.get(),
            departure_date_entry.get(),
            arrival_date_entry.get(),
            price_entry.get()
        ))
        add_button.grid(row=5, column=0, columnspan=2, pady=10)
    def ajouter_vol(self, departure_airport, arrival_airport, departure_date, arrival_date, price):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='AirlineDatabase',
                port=8889
            )
            with conn.cursor() as cursor:
                sql = "INSERT INTO Flight (Departure_Airport, Arrival_Airport, Departure_Date, Arrival_Date, Price) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (departure_airport, arrival_airport, departure_date, arrival_date, price))
            conn.commit()
            messagebox.showinfo("Success", "Flight added with success!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occur : {e}")
        finally:
            if conn:
                conn.close()

    def sales_analysis(self):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='AirlineDatabase',
                port=8889
            )

            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT DISTINCT Departure_Airport FROM Flight")
            arrival_airports = [airport['Departure_Airport'] for airport in cursor.fetchall()]

            labels = []
            values = []

            for airport in arrival_airports:
                cursor.execute("SELECT COUNT(*) as count FROM Flight WHERE Departure_Airport=%s", (airport,))
                result = cursor.fetchone()
                count = result['count'] if result else 0
                labels.append(airport)
                values.append(count)

            plt.figure(figsize=(12, 8))
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

        except Exception as e:
            messagebox.showerror("Error", f"Error in sales analysis: {e}")

        finally:
            cursor.close()
            conn.close()

    def redirect_to_account_information(self, event):
        self.accountPage_window = tk.Toplevel(self.root)
        self.app = AccountInformation.EmployeeAccount(self.accountPage_window)

    def redirect_to_edit_flight(self):
        try:
            config.departure_date = self.date_var.get()
            config.departure_airport = self.departure_var.get()
            config.arrival_airport = self.arrival_var.get()

            self.editFlight_window = tk.Toplevel(self.root)
            self.app = FlightBooking.FlightSelectionPage(self.editFlight_window,config.departure_date, config.departure_airport, config.arrival_airport)

        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")


    def redirect_to_user_info(self):
        try:
            config.email_info = self.email_var.get()

            self.user_info_window = tk.Toplevel(self.root)
            self.app = UserInfo.UserInfoPage(self.user_info_window,config.email_info)

        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def redirect_to_user_flight_history(self):
        try:
            user_email = self.email_var.get()

            if not user_email:
                messagebox.showwarning("Warning", "Please select a user's email.")
                return

            history_flight_window = tk.Toplevel(self.root)
            history_flight_window.title("Customer reservation history")
            history_flight_window.geometry("650x300")
            history_flight_window.configure(bg="white")

            self.main_frame = tk.Frame(history_flight_window, relief="solid", borderwidth=2)
            self.main_frame.pack(padx=10, pady=10)

            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='AirlineDatabase',
                port=8889
            )

            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT User_ID FROM User WHERE Email=%s", (user_email,))
            user_id = cursor.fetchone()

            if user_id:
                cursor.execute("SELECT * FROM Reservation WHERE User_ID=%s", (user_id['User_ID'],))
                reservations = cursor.fetchall()

                if reservations:
                    reservation_list = ttk.Treeview(self.main_frame, columns=(
                    "Flight_ID", "Departure_Date", "Departure_Airport", "Arrival_Airport", "Price"), show="headings",
                                                    selectmode="browse")

                    reservation_list.heading("Flight_ID", text="Flight ID")
                    reservation_list.column("Flight_ID", width=80)

                    reservation_list.heading("Departure_Date", text="Departure Date")
                    reservation_list.column("Departure_Date", width=150)

                    reservation_list.heading("Departure_Airport", text="Departure Airport")
                    reservation_list.column("Departure_Airport", width=150)

                    reservation_list.heading("Arrival_Airport", text="Arrival Airport")
                    reservation_list.column("Arrival_Airport", width=150)

                    reservation_list.heading("Price", text="Price")
                    reservation_list.column("Price", width=80)

                    reservation_list.pack(pady=20)

                    for reservation in reservations:
                        cursor.execute("SELECT * FROM Flight WHERE Flight_ID=%s", (reservation['Flight_ID'],))
                        flight_info = cursor.fetchone()
                        if flight_info:
                            reservation_list.insert("", "end", values=(
                            flight_info['Flight_ID'], flight_info['Departure_Date'], flight_info['Departure_Airport'],
                            flight_info['Arrival_Airport'], flight_info['Price']))

                else:
                    tk.Label(self.main_frame, text="No reservations found for this user.", font=("Helvetica", 12)).pack(
                        pady=20)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")

    def save(self):
        print("Vous avez enregistré")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeEmployee(root)
    root.mainloop()
