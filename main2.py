from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
import os
global filename

root= Tk()
root.title("Share-It")
root.geometry("450x560+500+200")
root.resizable(False,False)
def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#fdfdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='select Image File',
                                            filetype=(('file_type','*.txt*'),('All Files','*.*')))
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=3000
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any in comming connections.....')
        conn,addr=s.accept()
        print(conn)
        file=open(filename,'rb')
        print(file)
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully..")
    #icon
    image_icon=PhotoImage(file="send (1).png")
    window.iconphoto(False,image_icon)
    
    sbg=PhotoImage(file="sender.png")
    Label(window,image=sbg).place(x=-2,y=0)

    mbg=PhotoImage(file="id.png")
    Label(window,image=mbg,bg="#f4fdfe").place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f"ID: {host}",bg="white",fg="black").place(x=140,y=290)

    but=Button(window,text="+ select file",width=10,height=1,font="arial 14 bold",bg="#fff",fg="#000",command=select_file)
    but.place(x=160,y=150)

    but2=Button(window,text="SEND",width=10,height=1,font="arial 14 bold",bg="#000",fg="#fff",command=sender)
    but2.place(x=300,y=150)

    window.mainloop()


    
def Recieve():
    window2=Toplevel(root)
    window2.title("Receive")
    window2.geometry('450x560+500+200')
    window2.configure(bg="#fdfdfe")
    window2.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incomingID.get()

        s=socket.socket()
        port=3000
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
    #icon
    image_icon=PhotoImage(file="arrow.png")
    window2.iconphoto(False,image_icon)

   # hbg=PhotoImage(file="receiver.png")
   # Label(window2,image=hbg).place(x=-2,y=0)

    logo=PhotoImage(file="profile (1).png")
    Label(window2,image=logo,bg="#f4fdfe").place(x=10,y=260)

    Label(window2,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)

    Label(window2,text="Input Sender Id",font=('arial', 10,'bold'),bg='#f4fdfe').place(x=20,y=340)
    SenderID=Entry(window2,width=25,fg="black",border=2,bg="white",font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    
    Label(window2,text="File name for incoming file",font=('arial', 10,'bold'),bg='#f4fdfe').place(x=20,y=420)
    incomingID=Entry(window2,width=25,fg="black",border=2,bg="white",font=('arial',15))
    incomingID.place(x=20,y=450)

    image1_icon=PhotoImage(file="arrow (1).png")
    rr=Button(window2,image=image1_icon,text="Receive",compound=LEFT,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)


    window2.mainloop()


    
#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=30,y=40)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

img1=Image.open("send (1).png")
img1=img1.resize((40,40))
img2=ImageTk.PhotoImage(img1)
img1_bg=Button(root,image=img2,bg="#f4fdde",bd=0,command=Send).place(x=100,y=100)


img3=Image.open("arrow.png")
img3=img3.resize((40,40))
img4=ImageTk.PhotoImage(img3)
img3_bg=Button(root,image=img4,bg="#f4fdde",bd=0,command=Recieve).place(x=300,y=100)

Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="blue").place(x=90,y=160)
Label(root,text="Recieve",font=('Acumin Variable Concept',17,'bold'),bg="blue").place(x=280,y=160)

background=PhotoImage(file="background1.png")
Label(root,image=background).place(x=-2,y=323)






root.mainloop()