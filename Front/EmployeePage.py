import tkinter as tk

class HomeEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR ENGLAND: Home Page")

        self.bandeau_height = root.winfo_screenheight() * 0.22
        self.menu = None

        self.create_bandeau()

    def create_bandeau(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        title_label = tk.Label(self.root, text="Employee home page",font=("Arial", 20, "bold italic"), bg="white")
        title_label.place(x=self.bandeau_height * 3.2, y=self.bandeau_height * 0.4)

        image_path = "../Pictures/barre_recherche.png"
        self.image_button = tk.PhotoImage(file=image_path)
        image_button_label = tk.Label(self.root, image=self.image_button, cursor="hand2", bg="white")
        image_button_label.place(x=self.bandeau_height * 0.2, y=self.bandeau_height * 0.3)
        image_button_label.bind("<Button-1>", self.create_menu)

        image_path2 = "../Pictures/AirFly.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2, bg="white")
        image_label2.place(x=self.bandeau_height * 6.5, y=self.bandeau_height * 0.1)

        image_path3 = "../Pictures/Boreale.png"
        self.image3 = tk.PhotoImage(file=image_path3)
        image_label3 = tk.Label(self.root, image=self.image3, bg="white")
        image_label3.place(x=0, y=self.bandeau_height * 1.05, relwidth=1, relheight=0.75)

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

            flight_menu.add_command(label="flight available", command=self.save)
            flight_menu.add_command(label="flight discount offer", command=self.save)
            customer_menu.add_command(label="Customer file management", command=self.window_file_management)
            customer_menu.add_command(label="Customer reservation history", command=self.window_history_reservation)
            customer_menu.add_command(label="number of tickets purchased", command=self.save)
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

        submit_button = tk.Button(client_window, text="Submit", command=self.save)
        submit_button.pack()

    def save(self):
        print("Vous avez enregistré")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeEmployee(root)
    root.mainloop()
