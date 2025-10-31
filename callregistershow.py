import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

def showcallregistershow():
    t = tkinter.Tk()
    t.geometry('1300x800')
    t.title('Call Register')
    t.configure(bg="#ECF0F1")
    
    a = Text(t, height=40, width=150, font=("Courier", 10))
    a.place(x=20, y=20)
    
    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        msg = ''
        sql = "SELECT * FROM callregister"
        cur.execute(sql)
        data = cur.fetchall()

       
        msg += str("Call ID").ljust(10) + "\t"
        msg += str("Cus ID").ljust(15) + "\t"
        msg += str("Cat ID").ljust(15) + "\t"
        msg += str("Product ID").ljust(15) + "\t"
        msg += str("Eng ID").ljust(22) + "\t"
        msg += str("Estimash Charge").ljust(15) + "\n"
        msg += "-" * 97 + "\n"

        # 📋 Records
        for res in data:
            msg += str(res[0]).ljust(10) + "\t"
            msg += str(res[1]).ljust(15) + "\t"
            msg += str(res[2]).ljust(15) + "\t"
            msg += str(res[3]).ljust(15) + "\t"
            msg += str(res[4]).ljust(25) + "\t"
            msg += str(res[5]).ljust(15) + "\n"

        a.insert(END, msg)
        db.close()
      
    show()
    t.mainloop()