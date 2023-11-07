import tkinter as tk
from tkinter import messagebox
import pymysql
import subprocess
import platform

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Connexion")

        self.create_login_frame()

    def create_login_frame(self):
        login_frame = tk.Frame(self.root)
        login_frame.pack(pady=20)

        email_label = tk.Label(login_frame, text="Email")
        email_label.grid(row=0, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(login_frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(login_frame, text="Mot de passe")
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(login_frame, text="Se connecter", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.error_label = tk.Label(self.root, text="")
        self.error_label.pack()

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
            messagebox.showerror("Erreur", f"Erreur de base de données: {e}")
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
                messagebox.showerror("Erreur", f"Erreur lors de la redirection : {e}")
        else:
            self.error_label.config(text="Email ou mot de passe incorrect!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
