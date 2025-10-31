import tkinter
import pymysql
from tkinter import *

def showcallfeedbackshow():
    t = tkinter.Tk()
    t.geometry('1000x800')
    t.title('CALL FEEDBACK SHOW')
    t.configure(bg="#ECF0F1")

    a = Text(t, height=40, width=120, font=("Courier", 10))
    a.place(x=20, y=20)

    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        msg = ''

        sql = "SELECT * FROM callfeedback"
        cur.execute(sql)
        data = cur.fetchall()

        # 🧾 Header
        msg += str("Feedback ID").ljust(15) + "\t"
        msg += str("Feedback Rating").ljust(40) + "\t"
        msg += str("Remark").ljust(10) + "\n"
        msg += "-" * 80 + "\n"

        # 📋 Records
        for res in data:
            msg += str(res[0]).ljust(15) + "\t"
            msg += str(res[1]).ljust(40) + "\t"
            msg += str(res[2]).ljust(10) + "\n"

        a.insert(END, msg)
        db.close()

    show()
    t.mainloop()