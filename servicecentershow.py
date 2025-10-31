import tkinter
import pymysql
from tkinter import *

def showservicecentershow():
    t = Tk()
    t.geometry('1300x800')
    t.title("Service Center Show")
    a = Text(t, height=40, width=130, font=("Courier New", 12))
    a.place(x=20, y=20)

    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        sql = "SELECT * FROM servicecenter"
        cur.execute(sql)
        data = cur.fetchall()

        msg = ''
        
        msg += f"{'Office ID':<20}{'Name':<15}{'Address':<25}{'Phone':<25}{'Email':<22}{'Regno':>15}\n"
        msg += "-" * 130 + "\n"

    
        for res in data:
            msg += str(res[0]).ljust(10)      # ID
            msg += str(res[1]).ljust(25)      # Name
            msg += str(res[2]).ljust(25)      # Address
            msg += str(res[4]).ljust(25)      # Email 
            msg += str(res[3]).ljust(20)      # Phone
            msg += str(res[5]).rjust(9)       # Status
            msg += '\n'

        a.insert(END, msg)
        db.close()

    show()
    t.mainloop()