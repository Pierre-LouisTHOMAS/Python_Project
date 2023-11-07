from dbconnect import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
class customer():
    def __init__(self,id,name):
        self.__cust_id=id
        self.__cust_name=name

    def getcustid(self):
        return self.__cust_id
    def getcustname(self):
        return self.__cust_name
def myclick():
    print(useridval.get(),"  ",unameval.get())
    cust=customer(useridval.get(),unameval.get())
    print(db.fetch("Select * from customer"))
    #print(cust.getcustid())
    data=(cust.getcustid(),cust.getcustname())
    db.execute_row("insert into customer(custid,cname) values(%s,%s)",data)
    messagebox.showinfo("Important info","Data insreted successfully")


def viewrecords():
    row=db.fetch("Select custid,cname from customer")
    subwindow1=tkinter.Tk()
    subwindow1.geometry("500x300")
    subwindow1['bg']="light blue"
    tree = ttk.Treeview(subwindow1, column=("c1", "c2", "c3"), show='headings')
    tree.column("#1", anchor=tkinter.CENTER)
    tree.heading("#1", text="CustID")
    tree.column("#2", anchor=tkinter.CENTER)
    tree.heading("#2", text="CustNAME")
    tree.pack()
    for r in row:
        #print("here ",r["custid"])
        tree.insert("", tkinter.END, values=(r["custid"],r["cname"]))
        #tree.insert("", tkinter.END, values=)
    subwindow1.mainloop()
    mainwindow.destroy()

db=DBHelper()
db.connection()

mainwindow=tkinter.Tk()
mainwindow.geometry("500x300")
mainwindow['bg']="pink"

welcomelabel=tkinter.Label(mainwindow,text="WELCOME",font=('Helvetica 18 bold'))
welcomelabel.pack(anchor=tkinter.CENTER)
userid=tkinter.Label(mainwindow,text="User Id",pady=10)
userid.pack()
useridval=tkinter.Entry(text="userid",width=20)
useridval.pack()
username=tkinter.Label(mainwindow,text="User Name",pady=10)
username.pack()
unameval=tkinter.Entry(text="uname",width=20)
unameval.pack()
clickme=tkinter.Button(mainwindow,text="Save",command=myclick,bg="green")
clickme.pack()
viewdata=tkinter.Button(mainwindow,text="View records",command=viewrecords)
viewdata.pack()
mainwindow.mainloop()
#db.disconnect()