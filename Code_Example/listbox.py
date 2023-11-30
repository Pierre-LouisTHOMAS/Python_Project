from tkinter import *

# Create the root window
root = Tk()
root.geometry('180x200')

# Create a listbox
listbox = Listbox(root, width=40, height=10, selectmode="multiple")
#if selectmode is single then you choose only single item.
# Inserting the listbox items
listbox.insert(1, "London")
listbox.insert(2, "Paris")
listbox.insert(3, "Lisbon")
listbox.insert(4, "Barcelona")
listbox.insert(5, "Rome")

# selected listbox value(s)
def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))

# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='Select', command=selected_item)

# Placing the button and listbox
btn.pack(side='bottom')
listbox.pack()

root.mainloop()