import tkinter
import pymysql
from tkinter import *

def showcallcloseshow():
    t = tkinter.Tk()
    t.geometry('1000x800')
    t.title('Call - Close Show')
    t.configure(bg="#ECF0F1")

    a = Text(t, height=40, width=130, font=("Courier", 10))
    a.place(x=20, y=20)

    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        msg = ''

        sql = "SELECT * FROM callclose"
        cur.execute(sql)
        data = cur.fetchall()

        # 🧾 Header
        msg += str("Close ID").ljust(12) + "\t"
        msg += str("Call ID").ljust(15) + "\t"
        msg += str("Eng ID").ljust(20) + "\t"
        msg += str("Close Date").ljust(30) + "\n"
        msg += "-" * 60 + "\n"

        # 📋 Records
        for res in data:
            msg += str(res[0]).ljust(12) + "\t"
            msg += str(res[1]).ljust(15) + "\t"
            msg += str(res[2]).ljust(20) + "\t"
            msg += str(res[3]).ljust(30) + "\n"

        a.insert(END, msg)
        db.close()

    show()
    t.mainloop()