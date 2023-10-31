from tkinter import *

def choicemade():
   selection = "You selected the option to travel by " + str(var.get())+" class"
   label.config(text = selection)
root = Tk()
#var = IntVar()
var = StringVar(root,1)
R1 = Radiobutton(root, text="Business", variable=var, value="Business", command=choicemade)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Premium Economy", variable=var, value="Premium Economy", command=choicemade)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Economy", variable=var, value="Economy", command=choicemade)
R3.pack(anchor = W)
label = Label(root)
label.pack()
root.mainloop()



