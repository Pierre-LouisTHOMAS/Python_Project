import tkinter as tk
from Home_Page import AIRENGLANDApp  # Importez votre classe Page_Principale

def main():
    root = tk.Tk()
    app = AIRENGLANDApp(root)  # Créez l'instance de votre page principale ici
    root.mainloop()

if __name__ == "__main__":
    main()
