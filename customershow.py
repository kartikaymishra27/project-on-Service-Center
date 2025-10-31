import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

def showcustomershow():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Show Customer')
    t.configure(bg="#ECF0F1")
    a = Text(t, height=40, width=150)
    a.place(x=20, y=20)

    def show():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        msg=''
        sql="select * from customer"
        cur.execute(sql)
        data=cur.fetchall()

        msg += str("Customer ID").ljust(10) + "\t"
        msg += str("Customer Name").ljust(20) + "\t"
        msg += str("Address").ljust(20) + "\t"
        msg += str("Email").ljust(30) + "\t"
        msg += str("Phone").ljust(19) + "\t"
        msg += str("Category ID").ljust(25) + "\t"
        msg += str("Product ID").ljust(25) + "\t"
        msg += "\n" + "-" * 140 + "\n"

        for res in data:
            msg = msg + "\n" + str(res[0]).ljust(10) + "\t"
            msg = msg + str(res[1]).ljust(20) + "\t"
            msg = msg + str(res[2]).ljust(17) + "\t"
            msg = msg + str(res[3]).ljust(35) + "\t"
            msg = msg + str(res[4]).ljust(22) + "\t"
            msg = msg + str(res[5]).ljust(22) + "\t"
            msg = msg + str(res[6]).ljust(25) + "\t"

        a.insert(END,msg)
        db.close()

    show()
    t.mainloop()