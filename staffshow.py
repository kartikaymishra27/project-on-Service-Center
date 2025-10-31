import tkinter
import pymysql
from tkinter import *

def showstaffshow():
    t = tkinter.Tk()
    t.geometry('1400x700') 
    t.title("Staff Information")
    t.configure(bg="#ECF0F1")

    a = Text(t, height=40, width=160, font=("Courier", 10))  
    a.place(x=20, y=20)

    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        msg = ''
        sql = "SELECT * FROM staff"
        cur.execute(sql)
        data = cur.fetchall()

        msg += str("Staff ID").ljust(10) + "\t"
        msg += str("Staff Name").ljust(20) + "\t"
        msg += str("Address").ljust(20) + "\t"
        msg += str("Email").ljust(35) + "\t"
        msg += str("Phone").ljust(15) + "\n"
        msg += "-" * 100 + "\n"

        for res in data:
            msg += str(res[0]).ljust(10) + "\t"
            msg += str(res[1]).ljust(20) + "\t"
            msg += str(res[2]).ljust(20) + "\t"
            msg += str(res[3]).ljust(35) + "\t"
            msg += str(res[4]).ljust(15) + "\n"

        a.insert(END, msg)
        db.close()

    show()
    t.mainloop()