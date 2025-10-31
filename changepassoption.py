import tkinter as tk
from tkinter import messagebox
import pymysql
from loginotpsend import *
from passwordotpverify import *
from q_nverification import *
def showchangepasswordoption():
    t = tk.Tk()
    t.geometry('600x400')
    t.title("Login")
    t.configure(bg="#f0f2f5")
    
    
    
    title = tk.Label(t, text="Choose Option to Verify", font=("Segoe UI", 32, "bold"), fg="#0A3D62",bg="#f0f2f5")
    title.place(x=70, y=70)
    
    
    e=Label(t,text="Verify via Email :",font=("Segoe UI", 15, "bold"),fg="#0A3D62")
    e.place(x=90,y=200)
    btn = tk.Button(t, text="Email", bg="#0f4c75", fg="white",width=7,
                    font=("Segoe UI", 11, "bold"), relief="raised",
                    cursor="hand2",command=send_otp_window)
    btn.place(x=420, y=200)
    e=Label(t,text="Answer Security Questions :",font=("Segoe UI", 15, "bold"),fg="#0A3D62")
    e.place(x=90,y=270)
    signup_btn = tk.Button(t, text="Verify",width=7,
                          font=("Segoe UI", 11,"bold"),  bg="#0f4c75", fg="white", relief="raised",
                          cursor="hand2",command=show_security_verification)
    signup_btn.place(x=420, y=270)
    
    tk.Label(t, text="Contact support if you're stuck", font=("Helvetica", 9), fg="gray", bg="#f0f0f0").pack(side="bottom", pady=10)
    
    
    def on_enter(e): btn['bg'] = '#3282b8'
    def on_leave(e): btn['bg'] = '#0f4c75'
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    def on_enter(e): signup_btn['bg'] = '#3282b8'
    def on_leave(e): signup_btn['bg'] = '#0f4c75'
    signup_btn.bind("<Enter>", on_enter)
    signup_btn.bind("<Leave>", on_leave)
    
    
    
    t.mainloop()
