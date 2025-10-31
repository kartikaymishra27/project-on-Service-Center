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
from servicetypesdelete  import *
from servicetypesinsert import *
from servicetypesfind import *
from servicetypesshow import *
def servicetypesdashboard():
    t=tkinter.Tk()
    t.geometry('600x600')
    t.title("Servicetypes Dashboard")
   

    label = Label(t, text=" Service types ", font=('Segoe UI', 36, 'bold'), fg="black", bg="white")
    label.place(x=290, y=90, anchor='center') 
    
    # Insert Button
    btn = Button(t, text='Insert', font=('Arial', 18, 'bold'), bg='gray', fg='white', command=showservicetypesinsert)
    btn.place(x=120, y=210, width=130, height=50)

    # Delete Button
    btn1 = Button(t, text='Delete', font=('Arial', 18, 'bold'), bg='red', fg='white', command=showservicetypesdelete)
    btn1.place(x=330, y=210, width=130, height=50)

    # Find Button
    btn2 = Button(t, text='Find', font=('Arial', 18, 'bold'), bg='white', fg='black', command=showservicetypesfind)
    btn2.place(x=120, y=310, width=130, height=50)

    # Show Button
    btn3 = Button(t, text='Show', font=('Arial', 18, 'bold'), bg='teal', fg='white', command=showservicetypesshow)
    btn3.place(x=330, y=310, width=130, height=50)
    
    t.mainloop()
   
                
