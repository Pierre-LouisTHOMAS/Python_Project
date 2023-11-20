import tkinter as tk
import pymysql
import config

class UserInfoPage:
    def __init__(self, root, Email):
        self.root = root
        self.email = Email
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: User Info")

        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        canvas = tk.Canvas(root)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas, bg="lightblue")
        canvas.create_window((0, 0), window=frame, anchor="nw", width=root.winfo_screenwidth())

        content_frame = tk.Frame(frame, bg="lightblue")
        content_frame.pack(fill=tk.BOTH, expand=True)

        self.create_header(content_frame)
        self.create_user_info(content_frame)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def redirect_to_home_page(self, event):
        self.root.destroy()

    def create_header(self, frame):
        # logo picture
        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(8)
        image_label2 = tk.Label(frame, image=self.image2)
        image_label2.pack(side=tk.TOP, padx=10, pady=10)

        # Return to home page
        image_label2.bind("<Button-1>", self.redirect_to_home_page)

    def create_user_info(self, frame):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='AirlineDatabase',
            port=8889
        )
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = "SELECT User_ID, First_Name, Last_Name, Type, Category, Email, Password FROM User"

        where_conditions = []
        params = []

        if config.email_info:
            where_conditions.append("Email = %s")
            params.append(config.email_info)

        if where_conditions:
            query += " WHERE " + " AND ".join(where_conditions)

        cursor.execute(query, params)

        user_info = cursor.fetchall()

        for user in user_info:
            white_band = tk.Frame(frame, height=25, bg="white")
            white_band.pack(fill=tk.X)

            user_frame = tk.Frame(frame, borderwidth=2, relief=tk.GROOVE, bg="lightblue")
            user_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)

            user_ID_label = tk.Label(user_frame, text=f"User ID: {user['User_ID']}",
                                     font=("Arial", 14, "bold"), bg="lightblue")
            user_ID_label.grid(row=0, column=0, padx=(30, 40), pady=15, sticky="w")

            first_name_label = tk.Label(user_frame, text=f"First Name: {user['First_Name']}",
                                        font=("Arial", 11), bg="lightblue")
            first_name_label.grid(row=1, column=0, padx=(60, 40), pady=10, sticky="w")

            last_name_label = tk.Label(user_frame, text=f"Last Name: {user['Last_Name']}",
                                       font=("Arial", 14, "bold"), bg="lightblue")
            last_name_label.grid(row=0, column=1, padx=(30, 40), pady=15, sticky="w")

            type_label = tk.Label(user_frame, text=f"Type: {user['Type']}",
                                  font=("Arial", 11), bg="lightblue")
            type_label.grid(row=1, column=1, padx=(60, 40), pady=10, sticky="w")

            category_label = tk.Label(user_frame, text=f"Category: {user['Category']}",
                                      font=("Arial", 11), bg="lightblue")
            category_label.grid(row=1, column=1, padx=(60, 40), pady=10, sticky="w")

            email_label = tk.Label(user_frame, text=f"Email: {user['Email']}",
                                   font=("Arial", 11), bg="lightblue")
            email_label.grid(row=2, column=0, padx=(60, 40), pady=10, sticky="w")

            password_label = tk.Label(user_frame, text=f"Password: {user['Password']}",
                                      font=("Arial", 11), bg="lightblue")
            password_label.grid(row=2, column=1, padx=(60, 40), pady=10, sticky="w")

        cursor.close()
        conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoPage(root)
    root.mainloop()
