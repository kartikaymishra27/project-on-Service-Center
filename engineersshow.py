import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showengineersshow():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("Engineers Show")
    a = Text(t, height=40, width=110)
    a.place(x=20, y=20)
    def show():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        msg=''
        sql="select * from engineers"
        cur.execute(sql)
        data=cur.fetchall()
        
        msg += str("Eng ID").ljust(10) + "\t"
        msg += str("Eng Name").ljust(15) + "\t"
        msg += str("Address").ljust(19) + "\t"
        msg += str("Email").ljust(21) + "\t"
        msg += str("Phone").ljust(12) + "\t"
        msg += str("Category ID").ljust(10) + "\t"
       
        msg += "\n" + "-" * 95 + "\n"
        for res in data:
            msg = msg + "\n" + str(res[0]).ljust(10) + "\t"
            msg = msg + str(res[1]).ljust(15) + "\t"
            msg = msg + str(res[2]).ljust(15) + "\t"
            msg = msg + str(res[3]).ljust(25) + "\t"
            msg = msg + str(res[4]).ljust(15) + "\t"
            msg = msg + str(res[5]).ljust(10) + "\t"
    
        a.insert(END,msg)
        db.close()
      
    show()
    t.mainloop()