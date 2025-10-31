import tkinter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import random
import threading
import time
from tkinter import PhotoImage
import pymysql
from productsdelete  import *
from productsfind import *
from productsinsert import *
from productsshow import *
def productdashboard():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title("Products Dashboard")
    t.configure(bg="#ECF0F1")
   

    label = Label(t, text=" Products ", font=('Segoe UI', 36, 'bold'), fg="black", bg="white")
    label.place(x=290, y=90, anchor='center') 
    
    # Insert Button
    btn = Button(t, text='Insert', font=('Arial', 18, 'bold'), bg='gray', fg='white', command=showproductinsert)
    btn.place(x=120, y=210, width=130, height=50)

    # Delete Button
    btn1 = Button(t, text='Delete', font=('Arial', 18, 'bold'), bg='red', fg='white', command=showproductdelete)
    btn1.place(x=330, y=210, width=130, height=50)

    # Find Button
    btn2 = Button(t, text='Find', font=('Arial', 18, 'bold'), bg='white', fg='black', command=showproductfind)
    btn2.place(x=120, y=310, width=130, height=50)

    # Show Button
    btn3 = Button(t, text='Show', font=('Arial', 18, 'bold'), bg='teal', fg='white', command=showproductshow)
    btn3.place(x=330, y=310, width=130, height=50)
    
    exit_btn = Button(t, text="Exit", font=('Arial', 16, 'bold'), bg='#C0392B', fg='white', command=t.destroy)
    exit_btn.place(x=250, y=400, width=80, height=50)
    
    t.mainloop()
   
                
