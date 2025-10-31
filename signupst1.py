import tkinter as tk
from tkinter import messagebox
import pymysql
from loginotpsend import *
from forgetdashboardmain import *
import pyttsx3

t = tk.Tk()
t.geometry('1700x1400')
t.title("Login")
t.configure(bg="#f0f2f5")

def check():
    db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
    cur = db.cursor()
    xa = e1.get()
    xb = e2.get()
    if not xa or not xb:
        messagebox.showwarning("Missing Input", "Please enter both your username and password.")
        return



    sql = "select count(*) from logindata where loginid='%s' and password='%s'" % (xa, xb)
    cur.execute(sql)
    data = cur.fetchone()
   # ...

    if data[0] == 0:
       messagebox.showerror("Authentication Failed", "The username or password you entered is incorrect.\nPlease try again.")
    else:
       messagebox.showinfo("Login Successful", f"Welcome, {xa}!\nYou have been successfully logged in.")
       t.destroy()
       showotpsend()
    db.close()
engine = pyttsx3.init()
engine.say("Hello i am the assistant for you ")
engine.runAndWait()

title = tk.Label(t, text="Service Center Login", font=("Segoe UI", 32, "bold"), fg="#0A3D62", bg="white",relief="raised")
title.place(x=445, y=140)

a = tk.Label(t, text='Username:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5")
a.place(x=375, y=225)
e1 = tk.Entry(t, width=30, font=('Segoe UI', 17), bg="#f5f5f5", fg="#333333")
e1.place(x=575, y=240)

b = tk.Label(t, text='Password:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5")
b.place(x=375, y=285)
e2 = tk.Entry(t, width=30, font=('Segoe UI', 17), show="*", bg="#f5f5f5", fg="#333333")
e2.place(x=575, y=300)

c = tk.Label(t, text='Emails:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5")
c.place(x=375, y=335)
e2 = tk.Entry(t, width=30, font=('Segoe UI', 17), show="*", bg="#f5f5f5", fg="#333333")
e2.place(x=575, y=350)


show_pass = tk.IntVar()
signup_btn = tk.Button(t, text="Sign Up", 
                      font=("Segoe UI", 19,'bold'),  bg="#0f4c75", fg="white", relief="raised",padx=10, pady=5,
                      cursor="hand2")
signup_btn.place(x=525, y=450)


def toggle_password():
    if show_pass.get():
        e2.config(show='')
    else:
        e2.config(show='*')

chk = tk.Checkbutton(t, text="Show Password", variable=show_pass,
                     command=toggle_password, font=("Segoe UI", 12),
                     bg="#f0f2f5", activebackground="#f0f2f5")
chk.place(x=580, y=390)

def on_enter(e): signup_btn['bg'] = '#3282b8'
def on_leave(e): signup_btn['bg'] = '#0f4c75'
signup_btn.bind("<Enter>", on_enter)
signup_btn.bind("<Leave>", on_leave)


t.mainloop()
