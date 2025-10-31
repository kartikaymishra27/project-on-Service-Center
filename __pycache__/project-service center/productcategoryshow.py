import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showproductcategoryshow():
    t=tkinter.Tk()
    t.geometry('1200x1200')
    a = Text(t, height=40, width=90)
    a.place(x=20, y=20)
    def show():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        msg=''
        sql="select * from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            msg = msg + "\n" + str(res[0]).ljust(20) + "\t"
            msg = msg + str(res[1]).ljust(25) + "\t\t"
            msg = msg + str(res[2]).ljust(25) + "\t\t"
           
    
        a.insert(END,msg)
        db.close()
      
    show()
    t.mainloop()
