import tkinter
import smtplib
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import random
import threading
import time
from tkinter import PhotoImage
import pymysql
from maindashboard import *

t = tkinter.Tk()
t.geometry('600x400')
t.title("Login")
# t.configure(bg='#ccffcc') 

def check():
    db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
    cur = db.cursor()
    xa = e1.get()
    xb = e2.get()
    if not xa or not xb:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    sql = "select count(*) from logindata where loginid='%s' and password='%s'" % (xa, xb)
    cur.execute(sql)
    data = cur.fetchone()
    if data[0] == 0:
        messagebox.showinfo('Login Failed', 'User not found')
    else:
        messagebox.showinfo('Login Success', 'Welcome!')
        t.destroy()
        showdashboardservicecenter() 
    db.close()

# --- Title Placement Changed ONLY ---
title = Label(t, text="Service Center Login", font=("Segoe UI", 25, "bold") ,fg="#0A3D62", bg="white")
title.place(x=300, y=50,anchor='center')

# --- Username ---
a = Label(t, text='Username:', font=('arial', 18))
a.place(x=50, y=170)
e1 = Entry(width=30, font=('arial', 15))
e1.place(x=200, y=170)

# --- Password ---
b = Label(t, text='Password:', font=('arial', 18))
b.place(x=50, y=230)
e2 = Entry(width=30, font=('arial',15),show="*")
e2.place(x=200, y=230)
def toggle_password():
    if show_var.get():
        e2.config(show='')
    else:
        e2.config(show='*')

show_var = BooleanVar()
show_check = Checkbutton(t, text="Show Password", variable=show_var, command=toggle_password)
show_check.place(x=200, y=265)
# --- Button ---
btn = Button(t, text='Login', font=('arial', 15), bg='lightGray', command=check)
btn.place(x=260, y=320)

t.mainloop()
