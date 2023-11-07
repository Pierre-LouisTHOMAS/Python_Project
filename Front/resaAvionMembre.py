import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label

class ReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Réservation de Vol")

        self.bandeau_height = root.winfo_screenheight() * 0.20
        self.image2 = None
        self.image = None

        self.create_menu()
        self.create_bandeau()
        self.create_main_frame()

    def create_menu(self):
        self.menu = tk.Menu(self.root)

        fichier_menu = tk.Menu(self.menu, tearoff=0)
        fichier_menu.add_command(label="Enregistrer sous...", command=self.save)

        option_menu = tk.Menu(self.menu, tearoff=0)
        option_menu.add_command(label="Réglage")

        self.menu.add_cascade(label="Fichier", menu=fichier_menu)
        self.menu.add_cascade(label="Option", menu=option_menu)

        self.root.config(menu=self.menu)

    def save(self):
        print("Vous avez cliqué sur Enregistrer sous...")

    def create_bandeau(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=0.20)

        image_path2 = "../Pictures/AirFly.png"  # Remplacez par le chemin de votre image
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.bandeau_height * 0.7, y=self.bandeau_height * 0.1)

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, relief="solid", borderwidth=2)
        self.main_frame.grid(row=1, column=0, padx=10, pady=10)

        title_label = tk.Label(self.main_frame, text="Recherche de Vol", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        date_label = tk.Label(self.main_frame, text="Date de Départ")
        date_label.grid(row=1, column=0, pady=5)
        self.date_var = tk.StringVar()
        date_entry = DateEntry(self.main_frame, textvariable=self.date_var, date_pattern="dd/mm/yyyy")
        date_entry.grid(row=1, column=1, pady=5)

        departure_label = tk.Label(self.main_frame, text="Aéroport de Départ")
        departure_label.grid(row=2, column=0, pady=5)
        self.departure_var = tk.StringVar()
        departure_entry = tk.Entry(self.main_frame, textvariable=self.departure_var)
        departure_entry.grid(row=2, column=1, pady=5)

        arrival_label = tk.Label(self.main_frame, text="Aéroport d'Arrivée")
        arrival_label.grid(row=3, column=0, pady=5)
        self.arrival_var = tk.StringVar()
        arrival_entry = tk.Entry(self.main_frame, textvariable=self.arrival_var)
        arrival_entry.grid(row=3, column=1, pady=5)

        person_type_label = tk.Label(self.main_frame, text="Type de Personne")
        person_type_label.grid(row=4, column=0, pady=5)
        self.person_type_var = tk.StringVar()
        self.person_type_var.set("Adulte")
        person_type_option = tk.OptionMenu(self.main_frame, self.person_type_var, "Adulte", "Enfant")
        person_type_option.grid(row=4, column=1, pady=5)

        search_button = tk.Button(self.main_frame, text="Rechercher des Vols", command=self.search_flights)
        search_button.grid(row=6, column=0, columnspan=2, pady=10)

        image_path = "../Pictures/avionResa.png"  # Remplacez par le chemin de votre image
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(2)
        image_label = Label(self.main_frame, image=self.image)
        image_label.grid(row=0, column=2, rowspan=7, padx=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

    def search_flights(self):
        # Implement flight search logic here
        date = self.date_var.get()
        departure = self.departure_var.get()
        arrival = self.arrival_var.get()
        person_type = self.person_type_var.get()
        print(f"Date: {date}, Départ: {departure}, Arrivée: {arrival}, Type de Personne: {person_type}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationApp(root)
    root.mainloop()
