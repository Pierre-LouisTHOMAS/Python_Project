import tkinter as tk
from tkinter import Toplevel, messagebox, ttk
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

            if config.is_user_logged_in is False:
                config.user_discount = 0

            discount_factor = Decimal(config.user_discount) / 100
            config.total_price = flight['Price'] * Decimal(self.num_tickets) * (Decimal(1) - discount_factor)

            price_label2 = tk.Label(flight_frame, text=f"Economy ticket : {config.total_price:.2f}", font=("Arial", 12), bg="lightblue")
            price_label2.grid(row=0, column=5, padx=(20, 40), pady=15, sticky="w")
            reserve_button2 = tk.Button(flight_frame, text="Book", command=lambda f=flight: self.update_and_redirect(f), bg="lightblue")
            reserve_button2.grid(row=1, column=5, padx=(30, 40), pady=10, sticky="n")

            if config.user_type == 'Employee':
                modify_button = tk.Button(flight_frame, text="Modify", command=lambda f=flight: self.modify_flight(f), bg="red")
                modify_button.grid(row=1, column=6, padx=(10, 10), pady=10, sticky="n")
                delete_button = tk.Button(flight_frame, text="Delete", command=lambda f=flight: self.delete_flight(f), bg="red")
                delete_button.grid(row=1, column=7, padx=(10, 10), pady=10, sticky="n")

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
        modify_window = tk.Toplevel(self.root)
        modify_window.title(f"Modify Flight {flight['Flight_ID']}")
        modify_window.geometry("400x300")
        price_label = tk.Label(modify_window, text="Price")
        price_label.pack()
        price_entry = tk.Entry(modify_window)
        price_entry.pack()
        price_entry.insert(0, flight['Price'])
        departure_date_label = tk.Label(modify_window, text="Departure Date (YYYY-MM-DD HH:MM)")
        departure_date_label.pack()
        departure_date_entry = tk.Entry(modify_window)
        departure_date_entry.pack()
        departure_date_entry.insert(0, flight['Departure_Date'])
        arrival_date_label = tk.Label(modify_window, text="Arrival Date (YYYY-MM-DD HH:MM)")
        arrival_date_label.pack()
        arrival_date_entry = tk.Entry(modify_window)
        arrival_date_entry.pack()
        arrival_date_entry.insert(0, flight['Arrival_Date'])
        confirm_button = tk.Button(modify_window, text="Confirm", command=lambda: self.update_flight(flight['Flight_ID'],price_entry.get(),departure_date_entry.get(),arrival_date_entry.get(), flight['Departure_Airport'], flight['Arrival_Airport']))
        confirm_button.pack()
    def delete_flight(self, flight):
        confirmation = messagebox.askyesno("Delete Flight", f"Do you want to delete Flight {flight['Flight_ID']}?")
        if confirmation:
            try:
                conn = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    db='AirlineDatabase',
                    port=8889
                )
                with conn.cursor() as cursor:
                    sql = "DELETE FROM Flight WHERE Flight_ID = %s"
                    cursor.execute(sql, (flight['Flight_ID'],))
                conn.commit()
                messagebox.showinfo("Success", f"Flight {flight['Flight_ID']} deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                if conn:
                    conn.close()
    def update_flight(self, flight_id, new_price, new_departure_date, new_arrival_date, new_departure_airport, new_arrival_airport):
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='AirlineDatabase',
                port=8889
            )
            with conn.cursor() as cursor:
                sql = "UPDATE Flight SET Price = %s, Departure_Date = %s, Arrival_Date = %s, Departure_Airport = %s, Arrival_Airport = %s WHERE Flight_ID = %s"
                cursor.execute(sql, (
                new_price, new_departure_date, new_arrival_date, new_departure_airport, new_arrival_airport, flight_id))
            conn.commit()
            messagebox.showinfo("Success", "Flight updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()
    def select_return_flight(self, selected_flight):
        config.return_flight_bool = True
        self.propose_window.destroy()
        self.return_flight_window = tk.Toplevel(self.root)
        self.return_flight_window.title("Select Return Flight")
        self.return_flight_window.geometry("600x400")
        departure_airport = selected_flight['Arrival_Airport']
        arrival_airport = selected_flight['Departure_Airport']
        flight_list_frame = tk.Frame(self.return_flight_window)
        flight_list_frame.pack(fill=tk.BOTH, expand=True)
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Flight WHERE Departure_Airport = %s AND Arrival_Airport = %s",
                       (departure_airport, arrival_airport))
        flights = cursor.fetchall()
        if flights:
            for flight in flights:
                flight_info = f"Flight ID: {flight['Flight_ID']}, Departure: {flight['Departure_Date']}, Arrival: {flight['Arrival_Date']}, Price: {flight['Price']}"
                flight_button = tk.Button(flight_list_frame, text=flight_info, command=lambda f=flight: self.add_to_cart_and_redirect(f))
                flight_button.pack()
        else:
            no_flight_label = tk.Label(flight_list_frame, text="No flight available")
            no_flight_label.pack()
        cursor.close()
        conn.close()
    def propose_return_flight(self, selected_flight):
        self.propose_window = tk.Toplevel(self.root)
        self.propose_window.title("Book Return Flight")
        self.propose_window.geometry("300x200")
        label = tk.Label(self.propose_window, text="Do you want to book a return flight?")
        label.pack()
        yes_button = tk.Button(self.propose_window, text="Yes", command=lambda: self.select_return_flight(selected_flight))
        yes_button.pack()
        no_button = tk.Button(self.propose_window, text="No", command=lambda: self.redirect_to_book_flight())
        no_button.pack()
    def update_and_redirect(self, flight):
        config.selected_flight_id = flight['Flight_ID']
        config.selected_departure_date = flight['Departure_Date']
        config.selected_arrival_date = flight['Arrival_Date']
        config.selected_departure_airport = flight['Departure_Airport']
        config.selected_arrival_airport = flight['Arrival_Airport']
        config.selected_price = config.total_price

        config.cart['outbound_flight'] = {
            'Departure': config.selected_departure_airport,
            'Arrival': config.selected_arrival_airport,
            'Departure Time': config.selected_departure_date,
            'Arrival Time': config.selected_arrival_date,
            'Price': config.selected_price
        }

        self.outbound_flight_info = config.cart['outbound_flight']
        config.return_flight_bool = False

        self.propose_return_flight(flight)
    def add_to_cart_and_redirect(self, return_flight):
        self.return_flight_window.destroy()
        if not hasattr(config, 'cart'):
            config.cart = {'outbound_flight': None, 'return_flight': None}
        config.cart['outbound_flight'] = {
            'flight_id': config.selected_flight_id,
            'departure_date': config.selected_departure_date,
            'arrival_date': config.selected_arrival_date,
            'departure_airport': config.selected_departure_airport,
            'arrival_airport': config.selected_arrival_airport,
            'price': config.selected_price,
            'num_tickets': self.num_tickets
        }
        config.cart['return_flight'] = {
            'flight_id': return_flight['Flight_ID'],
            'departure_date': return_flight['Departure_Date'],
            'arrival_date': return_flight['Arrival_Date'],
            'departure_airport': return_flight['Departure_Airport'],
            'arrival_airport': return_flight['Arrival_Airport'],
            'price': return_flight['Price'],
            'num_tickets': self.num_tickets
        }

        self.redirect_to_book_flight()




    def redirect_to_book_flight(self):
        self.propose_window.destroy()
        self.bookFlight_window = tk.Toplevel(self.root)
        self.app = BookFlight.BookFlight(self.bookFlight_window)
    def reserve_flight(self, selected_flight):
        print(f"Selected Flight: Flight {selected_flight['flight_number']}, Departure: {selected_flight['departure']}, Arrival: {selected_flight['arrival']}")
if __name__ == "__main__":
    root = tk.Tk()
    app = FlightSelectionPage(root)
    root.mainloop()