import random
import threading
import time
from tkinter import PhotoImage, Tk, Label, Button
import pymysql
from dashboardproductcategory import *
from dashboardservicecenter import *
from dashboardengineers import *
from dashboardcustomer import *
from dashboardstaff import *
from dashboardcallregister import *
from dashboardcallclose import *
from dashboardcallfeedback import *
from dashboardproducts import *
from dashboardservicetypes import *
def showdashboardservicecenter():
    t = Tk()
    t.geometry('1000x680')
    t.title("Service Center ")

    # Header
    label = Label(t, text="Service Center", font=('Segoe UI', 36, 'bold'), fg="#0A3D62")
    label.pack(pady=20)

    # Left column buttons 1 to 5
    btn1 = Button(t, text='Service center', font=('Arial', 18, 'bold'), bg='#6A7B8C', fg='white', command=dashboardservicecenter)
    btn1.place(x=120, y=120, width=250, height=60)

    btn2 = Button(t, text='Product category', font=('Arial', 18, 'bold'), bg='#4682B4', fg='white', command=productcategorydashboard)
    btn2.place(x=120, y=200, width=250, height=60)

    btn3 = Button(t, text='Product', font=('Arial', 18, 'bold'), bg='#D3D3D3', fg='black',command=productdashboard)
    btn3.place(x=120, y=280, width=250, height=60)

    btn4 = Button(t, text='Services types', font=('Arial', 18, 'bold'), bg='#007070', fg='white',command=servicetypesdashboard)
    btn4.place(x=120, y=360, width=250, height=60)

    btn5 = Button(t, text='Customer', font=('Arial', 18, 'bold'), bg='pink', fg='white', command=customerdashboard)
    btn5.place(x=120, y=440, width=250, height=60)

    # Right column buttons 6 to 10
    btn6 = Button(t, text='Engineers', font=('Arial', 18, 'bold'), bg='#6A7B8C', fg='white', command=engineersdashboard)
    btn6.place(x=590, y=120, width=250, height=60)

    btn7 = Button(t, text='Staff', font=('Arial', 18, 'bold'), bg='#4682B4', fg='white', command=staffdashboard)
    btn7.place(x=590, y=200, width=250, height=60)

    btn8 = Button(t, text='Call register', font=('Arial', 18, 'bold'), bg='#D3D3D3', fg='black', command=callregisterdashboard)
    btn8.place(x=590, y=280, width=250, height=60)

    btn9 = Button(t, text='Call close', font=('Arial', 18, 'bold'), bg='#007070', fg='white', command=callclosedashboard)
    btn9.place(x=590, y=360, width=250, height=60)

    btn10 = Button(t, text='Call Feedback', font=('Arial', 18, 'bold'), bg='pink', fg='white', command=callfeedbackdashboard)
    btn10.place(x=590, y=440, width=250, height=60)

    # Exit Button
    exit_btn = Button(t, text="Exit", font=('Arial', 16, 'bold'), bg='#C0392B', fg='white', command=t.destroy)
    exit_btn.place(x=430, y=530, width=120, height=50)
   
    t.mainloop()


