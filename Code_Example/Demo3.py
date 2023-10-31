#To add image and icon to your page
import tkinter
import pymysql
from PIL import Image,ImageTk


root=tkinter.Tk()
root.geometry("500x300")
root['padx'] = 100
root['bg']="pink"
root.title("Welcome")
root.iconbitmap("C://Users//maith//Desktop//temp//flight.ico")

img= (Image.open("france.jpg"))
resized_image= img.resize((200,120),Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

mylabel=tkinter.Label(root,image=new_image)
mylabel.pack(padx=10)
#Adding radio buttons and check boxes


myButton=tkinter.Button(root,text="Click",command=test)
myButton.pack(side="bottom")
root.mainloop()









# Driver Code

# if __name__ == "__main__":
#
#     mysqlconnect()
