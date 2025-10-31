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
    label = Label(t, text="Service Center", font=("Segoe UI", 32, "bold"), fg="#0A3D62", bg="white", relief="raised")
    label.pack(pady=20)

   
    btn1 = Button(t, text='Service Center', font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=dashboardservicecenter)
    btn1.place(x=120, y=120, width=300, height=60)

    btn2 = Button(t, text='Product Category',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=productcategorydashboard)
    btn2.place(x=120, y=200, width=300, height=60)

    btn3 = Button(t, text='Product',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised",command=productdashboard)
    btn3.place(x=120, y=280, width=300, height=60)

    btn4 = Button(t, text='Services Types',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised",command=servicetypesdashboard)
    btn4.place(x=120, y=360, width=300, height=60)

    btn5 = Button(t, text='Customer', font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=customerdashboard)
    btn5.place(x=120, y=440, width=300, height=60)

    
    btn6 = Button(t, text='Engineers', font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=engineersdashboard)
    btn6.place(x=590, y=120, width=300, height=60)

    btn7 = Button(t, text='Staff',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=staffdashboard)
    btn7.place(x=590, y=200, width=300, height=60)

    btn8 = Button(t, text='Call Register',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=callregisterdashboard)
    btn8.place(x=590, y=280, width=300, height=60)

    btn9 = Button(t, text='Call Close',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=callclosedashboard)
    btn9.place(x=590, y=360, width=300, height=60)

    btn10 = Button(t, text='Call Feedback',  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=callfeedbackdashboard)
    btn10.place(x=590, y=440, width=300, height=60)

    # Exit Button
    exit_btn = Button(t, text="Close",  font=("Segoe UI", 28),  bg="#0f4c75", fg="white", relief="raised", command=t.destroy)
    exit_btn.place(x=430, y=530, width=150, height=50)
    
    def on_enter1(e): btn1['bg'] = '#3282b8'
    def on_leave1(e): btn1['bg'] = '#0f4c75'
    
    def on_enter2(e): btn2['bg'] = '#3282b8'
    def on_leave2(e): btn2['bg'] = '#0f4c75'
    
    def on_enter3(e): btn3['bg'] = '#3282b8'
    def on_leave3(e): btn3['bg'] = '#0f4c75'
    
    def on_enter4(e): btn4['bg'] = '#3282b8'
    def on_leave4(e): btn4['bg'] = '#0f4c75'
    
    def on_enter5(e): btn5['bg'] = '#3282b8'
    def on_leave5(e): btn5['bg'] = '#0f4c75'
    
    def on_enter6(e): btn6['bg'] = '#3282b8'
    def on_leave6(e): btn6['bg'] = '#0f4c75'
    
    def on_enter7(e): btn7['bg'] = '#3282b8'
    def on_leave7(e): btn7['bg'] = '#0f4c75'
    
    def on_enter8(e): btn8['bg'] = '#3282b8'
    def on_leave8(e): btn8['bg'] = '#0f4c75'
    
    def on_enter9(e): btn9['bg'] = '#3282b8'
    def on_leave9(e): btn9['bg'] = '#0f4c75'
    
    def on_enter10(e): btn10['bg'] = '#3282b8'
    def on_leave10(e): btn10['bg'] = '#0f4c75'
    
    def on_enter11(e):  exit_btn['bg'] = '#3282b8'
    def on_leave11(e):  exit_btn['bg'] = '#0f4c75'
    
    btn1.bind("<Enter>", on_enter1)
    btn1.bind("<Leave>", on_leave1)
    
    btn2.bind("<Enter>", on_enter2)
    btn2.bind("<Leave>", on_leave2)
    
    btn3.bind("<Enter>", on_enter3)
    btn3.bind("<Leave>", on_leave3)
    
    btn4.bind("<Enter>", on_enter4)
    btn4.bind("<Leave>", on_leave4)
    
    btn5.bind("<Enter>", on_enter5)
    btn5.bind("<Leave>", on_leave5)
    
    btn6.bind("<Enter>", on_enter6)
    btn6.bind("<Leave>", on_leave6)
    
    btn7.bind("<Enter>", on_enter7)
    btn7.bind("<Leave>", on_leave7)
    
    btn8.bind("<Enter>", on_enter8)
    btn8.bind("<Leave>", on_leave8)
    
    btn9.bind("<Enter>", on_enter9)
    btn9.bind("<Leave>", on_leave9)
    
    btn10.bind("<Enter>", on_enter10)
    btn10.bind("<Leave>", on_leave10)
    
    exit_btn.bind("<Enter>", on_enter11)
    exit_btn.bind("<Leave>", on_leave11)

       
    t.mainloop()