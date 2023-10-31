import tkinter

root = tkinter.Tk()
root.geometry("500x300")
root['bg']="pink"
mylabel=tkinter. Label (root, text="Welcome", font=('Helvetica 16 bold'))
mylabel.pack (anchor=tkinter.CENTER)
root.mainloop()