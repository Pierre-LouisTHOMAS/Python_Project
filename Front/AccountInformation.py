import tkinter as tk
from PIL import Image, ImageTk
import config

class EmployeeAccount:
    def __init__(self, root):
        self.root = root
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        self.root.title("Sky Travellers: Account Information")

        # Calculate dimensions
        self.header_height = root.winfo_screenheight() * 0.20
        self.window_width = root.winfo_screenwidth()
        self.window_height = root.winfo_screenheight()

        self.image2 = None
        self.image = None

        self.create_window()

    def redirect_to_home_page(self, event):
        self.root.destroy()

    def create_window(self):

        self.background_image = Image.open("../Pictures/bg3.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image.resize((self.window_width, self.window_height), Image.LANCZOS))
        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        self.main_frame = tk.Frame(self.root, relief="solid", borderwidth=2)
        self.main_frame.grid(row=1, column=1, padx=150, pady=15, sticky="e")

        image_path2 = "../Pictures/Logo.png"
        self.image2 = tk.PhotoImage(file=image_path2)
        self.image2 = self.image2.subsample(5)
        image_label2 = tk.Label(self.root, image=self.image2)
        image_label2.place(x=self.header_height * 0.7, y=self.header_height * 0.1)
        image_label2.bind("<Button-1>", lambda event: self.redirect_to_home_page(event))

        image_label2.bind("<Button-1>", self.redirect_to_home_page)

        title_label = tk.Label(self.main_frame, text="Employee Account", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        user_info_label = tk.Label(self.main_frame, text="User information:")
        user_info_label.grid(row=6, column=0, columnspan=2, pady=10)

        if config.user_type != 'Employee':
            user_info_text = f"First Name: {config.first_name_user}\nName: {config.last_name_user}\nType: {config.user_type}\nCategory: {config.member_category}"
        else:
            user_info_text = f"First Name: {config.first_name_user}\nName: {config.last_name_user}\nType: {config.user_type}"
        user_info_display = tk.Label(self.main_frame, text=user_info_text)
        user_info_display.grid(row=7, column=0, columnspan=2, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeAccount(root)
    root.mainloop()
