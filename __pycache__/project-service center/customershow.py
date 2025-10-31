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
    a = Text(t, height=40, width=150)
    a.place(x=20, y=20)
    def show():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        msg=''
        sql="select * from customer"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            msg = msg + "\n" + str(res[0]).ljust(10) + "\t"
            msg = msg + str(res[1]).ljust(20) + "\t"
            msg = msg + str(res[2]).ljust(20) + "\t"
            msg = msg + str(res[3]).ljust(15) + "\t"
            msg = msg + str(res[4]).ljust(25) + "\t"
            msg = msg + str(res[5]).ljust(25) + "\t"
    
        a.insert(END,msg)
        db.close()
      
    show()
    t.mainloop()