import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Toplevel, Entry, messagebox
import config
import pymysql

class PaymentWindow:
    def __init__(self, parent):
        self.parent = parent
        self.payment_window = Toplevel(parent)
        self.payment_window.geometry("400x300")
        self.payment_window.title("Payment Information")
        self.payment_window.configure(bg="#f0f0f0")

        vcmd = (self.payment_window.register(self.validate_input), "%P")

        tk.Label(self.payment_window, text="Card Number:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.card_number_entry = Entry(self.payment_window, validate="key", validatecommand=vcmd, font=("Helvetica", 12))
        self.card_number_entry.pack(pady=5)

        tk.Label(self.payment_window, text="Expiration Date:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.expiration_date_entry = Entry(self.payment_window, validate="key", validatecommand=vcmd, font=("Helvetica", 12))
        self.expiration_date_entry.pack(pady=5)

        tk.Label(self.payment_window, text="CVV:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.cvv_entry = Entry(self.payment_window, validate="key", validatecommand=vcmd, font=("Helvetica", 12), show="*")
        self.cvv_entry.pack(pady=5)

        tk.Button(self.payment_window, text="Submit Payment", command=self.process_payment, font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='white').pack(pady=10)

    def validate_input(self, value):
        return value.isdigit() or value == ""

    def process_payment(self):
        card_number = self.card_number_entry.get()
        expiration_date = self.expiration_date_entry.get()
        cvv = self.cvv_entry.get()

        if not all([card_number, expiration_date, cvv]):
            messagebox.showwarning("Warning", "Please fill in all payment details.")
            return

        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor()

        user_id = config.user_id
        flight_id = config.selected_flight_id
        number_of_tickets = 1
        total_payment = config.total_price

        query = "INSERT INTO Reservation (User_ID, Flight_ID, Number_of_Tickets, Total_Payment) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, flight_id, number_of_tickets, total_payment))

        conn.commit()

        messagebox.showinfo("Payment Successful", "Payment processed and reservation made successfully!")

        self.payment_window.destroy()

class BookFlight:
    def __init__(self, root, is_round_trip):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Book Page")

        self.header_height = root.winfo_screenheight() * 0.22
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()
        self.menu = None
        self.pay_button = None
        self.information_button = None

        self.root = root
        self.is_round_trip = is_round_trip

        self.outbound_flight_info = config.cart.get('outbound_flight', {})
        self.return_flight_info = config.cart.get('return_flight', {})

        self.create_window(is_round_trip)

    def display_flight_info(self, flight_info):
        labels_frame = tk.Frame(self.frame_flight, bg="white")
        labels_frame.pack()

        if flight_info:
            for key, value in flight_info.items():
                flight_label = tk.Label(labels_frame, text=f"{key}: {value}", bg="white", font=("Helvetica", 12))
                flight_label.pack(pady=2)
        else:
            no_flight_label = tk.Label(labels_frame, text="No flight information available", font=("Helvetica", 12), bg="white")
            no_flight_label.pack(pady=2)

    def redirect_to_flight_booking_page(self, event):
        self.root.destroy()




    def create_window(self, is_round_trip):
        self.background_image = Image.open("../Pictures/bg2.png")
        self.background_photo = ImageTk.PhotoImage(
            self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)   
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2, bg="white")
        image_label2.place(x=self.header_height * 6.5, y=self.header_height * 0.1)
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_flight_booking_page(event))

        frame_width = 400
        frame_height = 400
        self.frame_account = tk.Frame(self.root, bg="white", width=frame_width, height=frame_height, bd=2,
                                      relief=tk.GROOVE)
        self.frame_account.place(relx=0.5, rely=0.5, anchor='center')

        self.frame_flight = tk.Frame(self.root, bg="white", width=frame_width, height=frame_height, bd=2,
                                     relief=tk.GROOVE)
        self.frame_flight.place(relx=0.2, rely=0.5, anchor='center')

#Aller et retour
        if is_round_trip:
            flight_info_label = tk.Label(self.frame_flight, text="Flight Information", font=("Helvetica", 16, "bold"),
                                     bg="white")
            flight_info_label.pack(pady=20)
            tk.Label(self.frame_flight, text="Outbound Flight Information", font=("Helvetica", 12, "bold"),
                 bg="white").pack(pady=5)
            self.display_flight_info(self.outbound_flight_info)
            tk.Label(self.frame_flight, text="Return Flight Information", font=("Helvetica", 12, "bold"), bg="white").pack(
            pady=5)
            self.display_flight_info(self.return_flight_info)
            departure_airport = config.cart.get('outbound_flight', {}).get('Departure', '')
            arrival_airport = config.cart.get('outbound_flight', {}).get('Arrival', '')
            departure_time = config.cart.get('outbound_flight', {}).get('Departure Time', '')
            arrival_time = config.cart.get('outbound_flight', {}).get('Arrival Time', '')
            price = config.cart.get('outbound_flight', {}).get('Price', '')

            config.cart['outbound_flight'] = {
                'Departure': departure_airport,
                'Arrival': arrival_airport,
                'Departure Time': departure_time,
                'Arrival Time': arrival_time,
                'Price': price
            }

            self.warning_label = tk.Label(self.frame_flight, text="", font=("Helvetica", 12), bg="white", fg="red")
            self.warning_label.pack(pady=5)

    #si pas retour
        else:
            departure_airport = config.selected_departure_airport
            arrival_airport = config.selected_arrival_airport
            departure_time = config.selected_departure_date
            arrival_time = config.selected_arrival_date
            price = config.total_price

            labels_frame = tk.Frame(self.frame_account, bg="white")
            labels_frame.pack()
            departure_label = tk.Label(labels_frame, text=f"Departure: {departure_airport}", bg="white",
                                       font=("Helvetica", 12))
            departure_label.pack(pady=5)
            arrival_label = tk.Label(labels_frame, text=f"Arrival: {arrival_airport}", bg="white",
                                     font=("Helvetica", 12))
            arrival_label.pack(pady=5)
            departure_time_label = tk.Label(labels_frame, text=f"Departure Time: {departure_time}", bg="white",
                                            font=("Helvetica", 12))
            departure_time_label.pack(pady=5)
            arrival_time_label = tk.Label(labels_frame, text=f"Arrival Time: {arrival_time}", bg="white",
                                          font=("Helvetica", 12))
            arrival_time_label.pack(pady=5)
            price_label = tk.Label(self.frame_account, text=f"Price: {price}", bg="white",
                                   font=("Helvetica", 14, "bold"))
            price_label.pack(pady=10)
            self.warning_label = tk.Label(self.frame_account, text="", font=("Helvetica", 12), bg="white", fg="red")
            self.warning_label.pack(pady=5)

        if not config.is_user_logged_in:
            self.information_button = tk.Button(self.frame_account, text="Information", command=self.show_questionnaire,
                                                font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='white')
            self.information_button.pack(pady=5)

            self.pay_button = tk.Button(self.frame_account, text="Pay", command=self.open_payment_window,
                                        font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='white', state=tk.DISABLED)
            self.pay_button.pack(pady=5)
        else:
            self.show_user_info()
            self.pay_button = tk.Button(self.frame_account, text="Pay", command=self.open_payment_window,
                                        font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='white')
            self.pay_button.pack(pady=5)

    def validate_questionnaire(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()

        if not all([first_name, last_name, email]):
            self.warning_label.config(text="Please fill in all fields in the questionnaire.", fg="red")
            return False
        else:
            self.warning_label.config(text="")
            return True

    def open_payment_window(self):
        PaymentWindow(self.root)

    def show_user_info(self):
        user_info_text = f"First Name: {config.first_name_user}\nName: {config.last_name_user}\nType: {config.user_type}\nCategory: {config.member_category}"
        user_info_display = tk.Label(self.frame_account, text=user_info_text, font=("Helvetica", 12), bg="white")
        user_info_display.pack(pady=5)

    def show_questionnaire(self):
        questionnaire_window = tk.Toplevel(self.root)
        questionnaire_window.geometry("400x300")
        questionnaire_window.title("Questionnaire")
        questionnaire_window.configure(bg="#f0f0f0")

        tk.Label(questionnaire_window, text="First Name:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.first_name_entry = Entry(questionnaire_window, font=("Helvetica", 12))
        self.first_name_entry.pack(pady=5)

        tk.Label(questionnaire_window, text="Last Name:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.last_name_entry = Entry(questionnaire_window, font=("Helvetica", 12))
        self.last_name_entry.pack(pady=5)

        tk.Label(questionnaire_window, text="Email:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
        self.email_entry = Entry(questionnaire_window, font=("Helvetica", 12))
        self.email_entry.pack(pady=5)

        def get_questionnaire_info():
            try:
                if not self.validate_questionnaire():
                    return

                first_name = self.first_name_entry.get()
                last_name = self.last_name_entry.get()
                email = self.email_entry.get()

                conn = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    db='AirlineDatabase',
                    port=8889
                )
                cursor = conn.cursor()

                query = "INSERT INTO User (First_Name, Last_Name, Type, Category, Email) VALUES (%s, %s, %s, %s, %s)"

                cursor.execute(query, (first_name, last_name, 'Guest', 'NULL', email))
                conn.commit()

                user_info_text = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}"
                user_info_display = tk.Label(self.frame_account, text=user_info_text, font=("Helvetica", 12),
                                             bg="white")
                user_info_display.pack(pady=5)

                self.information_button.configure(state=tk.DISABLED)

                self.pay_button.configure(state=tk.NORMAL)

                questionnaire_window.destroy()

            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                cursor.close()
                conn.close()

        submit_button = tk.Button(questionnaire_window, text="Submit", command=get_questionnaire_info,
                                 font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='white')
        submit_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookFlight(root)
    root.mainloop()
