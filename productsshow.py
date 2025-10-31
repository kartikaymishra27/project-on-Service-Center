import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showproductshow():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product show')
    a = Text(t, height=40, width=90)
    a.place(x=20, y=20)
    def show():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        msg=''
        sql="select * from products"
        cur.execute(sql)
        data=cur.fetchall()
        msg = ''
        
        msg += f"{'Product ID':<20}{'Product Name':<25}{'Category Name':<25}{'Warranty Days':<25}\n"
        msg += "-" * 90 + "\n"
        for res in data:
            msg = msg + "\n" + str(res[0]).ljust(20) + "\t"
            msg = msg + res[1].ljust(25) + "\t"
            msg = msg + res[2].ljust(25) + "\t"
            msg = msg + res[3].ljust(25) + "\t"
           
    
        a.insert(END,msg)
        db.close()
      
    show()
    t.mainloop()