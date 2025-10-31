import tkinter
import pymysql
from tkinter import *

def showproductcategoryshow():
    t = tkinter.Tk()
    t.geometry('800x800')
    t.title("Product Category Show")

    a = Text(t, height=40, width=120, font=("Courier New", 12))
    a.place(x=20, y=20)

    def show():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        sql = "SELECT * FROM productcategory"
        cur.execute(sql)
        data = cur.fetchall()

        msg = ''
        # Header text
        header = f"{'Category ID':<15}{'Category Name':<25}{'Description':<40}"

        # Center the header by calculating padding
        total_width = 80  # Width of the Text widget
        padding = (total_width - len(header)) // 2
        msg += " " * padding + header + "\n"
        msg += "-" * total_width + "\n"

        # Row Data (aligned with ljust for consistent spacing)
        for res in data:
            row = ''
            row += str(res[0]).ljust(15)
            row += str(res[1]).ljust(25)
            row += str(res[2]).ljust(38)
            msg += row + "\n"

        a.insert(END, msg)
        db.close()

    show()
    t.mainloop()