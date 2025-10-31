import tkinter as tk
from tkinter import messagebox
from maindashboard import showdashboardservicecenter
from loginotpsend import *

def showotpverify(email):
    t = tk.Tk()
    t.geometry('600x400')
    t.title('Verify OTP')
    t.configure(bg='#f0f2f5')

    show_pass = tk.IntVar()

    def verify():
        entered_email = e1.get().strip()
        entered_otp = e2.get().strip()

        if not entered_email or not entered_otp:
            messagebox.showwarning("Input Required", "Please fill in both fields to verify.")
            return

        try:
            with open('myotpproject.txt', 'r') as f:
                content = f.read().strip()
        except FileNotFoundError:
            messagebox.showerror("File Error", "OTP data file not found.")
            return

        parts = content.split()
        if len(parts) != 2:
            messagebox.showerror("Data Error", "Stored OTP data is corrupted or incomplete.")
            return

        saved_email, saved_otp = parts

        if entered_email == saved_email and entered_otp == saved_otp:
            messagebox.showinfo("Verification Successful", f"OTP {entered_otp} has been verified successfully.")
            t.destroy()
            showdashboardservicecenter()
        else:
            messagebox.showwarning("Verification Failed", "The OTP you entered is incorrect. Please try again.")

    # --- UI Elements ---
    tk.Label(t, text="OTP Verification", font=("Segoe UI", 25, "bold"),relief="raised",
             fg="#0A3D62", bg="white").place(x=300, y=50, anchor='center')

    tk.Label(t, text='Email:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5").place(x=50, y=155)
    e1 = tk.Entry(t, width=30, font=('Segoe UI', 17), bg="#f5f5f5", fg="#333333")
    e1.place(x=200, y=170)
    e1.insert(0, email)

    tk.Label(t, text='OTP:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5").place(x=50, y=215)
    e2 = tk.Entry(t, width=30, font=('Segoe UI', 17), bg="#f5f5f5", fg="#333333", show='*')
    e2.place(x=200, y=230)

    def toggle_password():
        e2.config(show='' if show_pass.get() else '*')

    chk = tk.Checkbutton(t, text="Show OTP", variable=show_pass,relief="raised", command=toggle_password,
                         font=("Segoe UI", 12), bg="#f0f2f5", activebackground="#f0f2f5")
    chk.place(x=200, y=280)

    btn1 = tk.Button(t, text='Verify OTP', bg="#0f4c75", fg="white",relief="raised",
                     font=("Segoe UI", 15, "bold"), padx=10, pady=5,
                     cursor="hand2", command=verify)
    btn1.place(x=300, y=360, anchor='center')

    def on_enter(e): btn1['bg'] = '#3282b8'
    def on_leave(e): btn1['bg'] = '#0f4c75'
    btn1.bind("<Enter>", on_enter)
    btn1.bind("<Leave>", on_leave)

    t.mainloop()
