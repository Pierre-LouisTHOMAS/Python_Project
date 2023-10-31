import tkinter
def myclick():
    pass

root = tkinter.Tk()
root.geometry("500x300")
root['bg'] = "pink"
mylabel=tkinter.Label(root,text="Welcome", font=('Helvetica 16 bold'))
mylabel.pack(anchor=tkinter.CENTER)
userid=tkinter.Label(root,text="User ID", pady=10)
userid.pack()
txtuserid=tkinter.Entry(text="ID")
txtuserid.pack()
logme=tkinter.Button(root,text="Log me IN", command=myclick,bg="green")
logme.pack()

root.mainloop()
