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

        # Création de la fenêtre principale
        analysis_window = tk.Toplevel(self.root)
        analysis_window.title("Sales Analysis")

        # Création de la liste déroulante
        options = ["Aéroport de départ", "Aéroport d'arrivée"]
        selected_option = tk.StringVar()
        combo = ttk.Combobox(analysis_window, values=options, textvariable=selected_option)
        combo.pack(side=tk.LEFT, padx=10, pady=10)

        # Fonction pour générer le graphe en fonction de la sélection
        def generate_graph():
            try:
                selected_value = selected_option.get()
                if selected_value == "Aéroport de départ":
                    cursor.execute("SELECT DISTINCT Departure_Airport FROM Flight")
                    airports = [airport['Departure_Airport'] for airport in cursor.fetchall()]
                    label_text = "Departure_Airport"
                else:
                    cursor.execute("SELECT DISTINCT Arrival_Airport FROM Flight")
                    airports = [airport['Arrival_Airport'] for airport in cursor.fetchall()]
                    label_text = "Arrival_Airport"

                labels = []
                values = []

                for airport in airports:
                    cursor.execute("SELECT COUNT(*) as count FROM Flight WHERE {}=%s".format(label_text), (airport,))
                    result = cursor.fetchone()
                    count = result['count'] if result else 0
                    labels.append(airport)
                    values.append(count)

                plt.figure(figsize=(12, 8))
                plt.bar(labels, values)
                plt.xlabel("City")
                plt.ylabel("Number of flights")
                plt.title("Flight analysis - {}".format(label_text))

                # Création de la fenêtre du graphe
                graph_window = tk.Toplevel(self.root)
                graph_window.title("Flight analysis Graph")

                canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            except Exception as e:
                messagebox.showerror("Error", f"Error in generate_graph: {e}")

        # Bouton pour générer le graphe
        generate_button = tk.Button(analysis_window, text="Generate Graph", command=generate_graph)
        generate_button.pack(side=tk.LEFT, padx=10, pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Error in sales analysis: {e}")

    finally:
        # Ne fermez pas le curseur ici
        # cursor.close()
        conn.close()