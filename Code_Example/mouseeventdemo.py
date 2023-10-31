from tkinter import *
def mouseEntered(event):
 button = event.widget
 button.config(text = "Please Please click me")
def mouseExited(event):
 button = event.widget
 button.config(text = "Logon")
def main():
 global root
 root = Tk() # Create the root (base) window where all widgets go
 b = Button(root, text="Logon")
 b.bind("<Enter>",mouseEntered)
 b.bind("<Leave>",mouseExited)
 b.pack()
 root.mainloop() # Start the event loop
main()