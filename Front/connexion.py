import tkinter as tk
from tkinter import messagebox
import pymysql
import subprocess
import platform

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("AIR FLY: Login")

        self.create_login_frame()
        self.create_image_frame()


    def redirect_to_page_accueil(self, event):
        root.destroy()
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(["python", "Page_Principale.py"], shell=True)
            else:
                subprocess.Popen(["python3", "Page_Principale.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection : {e}")

    def create_login_frame(self):
        # Create a frame for the black box and centre it in the window
        login_frame = tk.Frame(self.root, borderwidth=3, relief="solid", width=300, height=100)
        login_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a sub-frame for the form and centre it inside the black frame
        form_frame = tk.Frame(login_frame)
        form_frame.grid(row=0, column=0, padx=500, pady=20)

        email_label = tk.Label(form_frame, text="Email")
        email_label.grid(row=0, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(form_frame, text="Mot de passe")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(form_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(form_frame, text="Se connecter", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.error_label = tk.Label(form_frame, text="")
        self.error_label.grid(row=3, column=0, columnspan=2, pady=10)

    def create_image_frame(self):
        # Create a frame for the image and use pack to centre it
        image_frame = tk.Frame(self.root)
        image_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.root.grid_columnconfigure(1, weight=1)

        image = tk.PhotoImage(file="../Pictures/AirFly.png")
        image_label = tk.Label(image_frame, image=image)
        image_label.image = image
        image_label.pack()

        #Return to home page
        image_label.bind("<Button-1>", self.redirect_to_page_accueil)
    def verify_login(self, email, password):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Client WHERE email = %s AND password = %s", (email, password))
                result = cursor.fetchone()
                return result is not None
        except Exception as e:
            messagebox.showerror("Error", f"Error on redirection {e}")
            return False
        finally:
            conn.close()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if self.verify_login(email, password):
            self.root.destroy()
            try:
                if platform.system() == 'Windows':
                    subprocess.Popen(["python", "Page_Principale.py"], shell=True)
                else:
                    subprocess.Popen(["python3", "Page_Principale.py"])
            except Exception as e:
                messagebox.showerror("Error", f"Error on redirection {e}")
        else:
            self.error_label.config(text="Email ou mot de passe incorrect!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
