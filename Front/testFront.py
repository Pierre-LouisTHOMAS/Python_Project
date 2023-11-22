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