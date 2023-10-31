import tkinter
import pymysql


def myclick():
    uname=unametxt.get()
    pwd=pwdtxt.get()
    print(pwd)
    conn = pymysql.connect(

    host='localhost',

    user='root',

    password="",

    db='myproject',

    )

    print(int(uname))
    #Change the name of the table as per requirement

    cur = conn.cursor()

    row_cnt=cur.execute("select cname from customer where custid='%s'",int(uname))

    output = cur.fetchall()
    if (row_cnt==0):
        print("No user")
    else:
        root1=tkinter.Tk()
        root1.geometry("500x300")
        root1['padx'] = 0
        myLabel2=tkinter.Label(root1, text="Hello ",font= ('Helvetica 12'))
        myLabel2.grid(row=0 column=0)
        uname2=tkinter.Label(root1, text=unametxt.get(),pady=10)
        uname2.grid(row=0 column=1)

        unametxt2=tkinter.Entry(root1,text="Values")
        unametxt2..grid(row=1 column=1)
        Login2=tkinter.Button(root1, text="Click me ",bg="green")
        Login2.grid(row=2 column=1)



    root1.mainloop()

    conn.close()








root=tkinter.Tk()
root.geometry("500x300")
root['padx'] = 0
#root['bg']="pink"
#create a label widget
myLabel1=tkinter.Label(root, text="Welcome to my page1",font= ('Helvetica 18 bold'))
myLabel1.pack(anchor=tkinter.CENTER)
uname=tkinter.Label(root, text="UserName",pady=10)
uname.pack()
unametxt=tkinter.Entry(text="Enter Username")
unametxt.pack()
pwd=tkinter.Label(root, text="Password",pady=10)

pwd.pack()
pwdtxt=tkinter.Entry(text="Enter Password",width=25, font=('Calibri 14'))
pwdtxt.pack()

# # Echoing password and masked with hashtag(#)
# import maskpass  # importing maskpass library
#
# # prompt msg = Password and
# # masking password with hashtag(#)
# pwd = maskpass.askpass(prompt="Password:", mask="#")
# print(pwd)
Login=tkinter.Button(root, text="Log me in",command=myclick,bg="pink")
Login.pack()
root.mainloop()


