import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
def showpass():
    def verify():
        login_id=entry_login.get().strip().lower()
        email_id=entry_email.get().strip().lower()
        password=entry_verify.get().strip().lower()
        
        if not login_id and not email_id and  password:
            messagebox.showinfo("Data found", "enter all value")
        if len(password) <8:
            messagebox.showinfo("Data found", "password should be 8 digit ")
            return
        
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        cur.execute("UPDATE logindata SET password = %s WHERE loginid = %s", (password, login_id))
        db.commit()
        messagebox.showinfo(
        "Password Updated",
        f"Dear {login_id},\n\n"
        f"Your password has been updated successfully.\n"
        f"New Password: {password}\n\n"
        "For your account's security:\n"
        "- Never share your password with anyone.\n"
        "- Choose a strong password that includes letters, numbers, and symbols.\n"
        "- You may now log in with your new password.\n\n"
        "Thank you for using our Service Center."
    )
    
        db.close()
            
        
        
        
        
    root = Tk()
    root.geometry('600x440')
    root.title('Send & Verify OTP - Service Center')
    root.configure(bg='#f0f2f5')
    
    
        
    
     
    heading = Label(root, text="Secure OTP Verification", font=("Segoe UI", 28, "bold"), fg="#0A3D62", bg="#f0f2f5")
    heading.place(x=300, y=40, anchor='center')
    
    Label(root, text='User ID:', font=("Segoe UI", 16), fg="#333333", bg="#f0f2f5").place(x=50, y=100)
    entry_login = Entry(root, width=30, font=('Segoe UI', 14), bg="#ffffff", fg="#333333")
    entry_login.place(x=200, y=105)
    
    Label(root, text='Email:', font=("Segoe UI", 16), fg="#333333", bg="#f0f2f5").place(x=50, y=150)
    entry_email = Entry(root, width=30, font=('Segoe UI', 14), bg="#ffffff", fg="#333333")
    entry_email.place(x=200, y=155)
    
    Label(root, text='Password:', font=("Segoe UI", 16), fg="#333333", bg="#f0f2f5").place(x=50, y=200)
    entry_verify = Entry(root, width=30, font=('Segoe UI', 14), bg="#ffffff", fg="#333333", show='*')
    entry_verify.place(x=200, y=205)
    
    show_var = IntVar()
    def toggle_password():
        entry_verify.config(show='' if show_var.get() else '*')
    
    chk = Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password,
                       font=("Segoe UI", 12), bg="#f0f2f5", activebackground="#f0f2f5")
    chk.place(x=200, y=240)
    
    btn_change = Button(root, text='Change Password', bg="#0f4c75", fg="white",
                       font=("Segoe UI", 14, "bold"), padx=10, pady=5,
                       cursor="hand2",command=verify)
    btn_change.place(x=150, y=330)
    
    
    def on_enter(e): btn_change['bg'] = '#3282b8'
    def on_leave(e): btn_change['bg'] = '#0f4c75'
    btn_change.bind("<Enter>", on_enter)
    btn_change.bind("<Leave>", on_leave)
    
    
    root.mainloop()