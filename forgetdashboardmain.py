import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
from maindashboard import showdashboardservicecenter
from changepassoption import *

def send_otp_window():
    root = Tk()
    root.geometry('600x400')
    root.title('Send & Verify OTP - Service Center')
    root.configure(bg='#f0f2f5')

    def send_otp():
        login_id = entry_login.get().strip()

        if not login_id:
            messagebox.showwarning("Missing Info", "Please enter your User ID.")
            return

        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
            cur = db.cursor()
            cur.execute("SELECT email FROM logindata WHERE loginid = %s", (login_id,))
            result = cur.fetchone()

            if not result:
                messagebox.showerror("Not Found", f"No account found with ID '{login_id}'.")
                return

            to_address = result[0]
            from_address = "luckymishra741756@gmail.com"
            otp = random.randint(100000, 999999)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Secure OTP for Your Authorized Access - Service Center"
            msg['From'] = from_address
            msg['To'] = to_address

            html = f"""
            <html>
              <body style="font-family: 'Segoe UI', sans-serif; background-color: #f4f6f7; color: #2c3e50;">
                <div style="padding: 25px; border: 1px solid #dcdde1; border-radius: 10px; background-color: #ffffff; max-width: 650px; margin: auto;">
                  <h2 style="color: #1e3799; text-align: center;">OTP for Authorized Account Verification</h2>
                  <p>Dear User,</p>
                  <p>You have requested secure access to your Service Center account. Use the OTP below to verify:</p>
                  <p style="font-size: 26px; font-weight: bold; color: #e74c3c; text-align: center;">{otp}</p>
                  <p>This OTP is valid for one-time use only. Please do not share it with anyone.</p>
                  <hr>
                  <p>Support: <strong>luckymishra741756@gmail.com</strong></p>
                  <p>Regards,<br><strong>Service Center Team</strong></p>
                </div>
              </body>
            </html>
            """

            msg.attach(MIMEText(html, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, 'nttx dlfy rcpr gyce')
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()

            with open('passwordotp.txt', 'w') as f:
                f.write(login_id + ' ' + str(otp))

            
            masked_email = to_address
            if '@' in masked_email:
                name, domain = masked_email.split('@')
                if len(name) > 6:
                    masked_email = (
                        name[:3] + '*' * (len(name) - 6) + name[-3:] + '@' + domain
                    )
                elif len(name) > 3:
                    masked_email = (
                        name[:3] + '*' * (len(name) - 3) + '@' + domain
                    )
                else:
                    masked_email = '*' * len(name) + '@' + domain
            
            messagebox.showinfo(
                'OTP Sent',
                f'Dear Valued {login_id} \nOTP has been sent successfully to your registered email:\n {masked_email}'
            )


        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def verify():
        entered_id = entry_login.get().strip()
        entered_otp = entry_verify.get().strip()

        if not entered_id or not entered_otp:
            messagebox.showwarning("Missing Info", "Enter both User ID and OTP to verify.")
            return

        try:
            with open('passwordotp.txt', 'r') as f:
                content = f.read().strip()
        except FileNotFoundError:
            messagebox.showerror("File Error", "OTP data file not found.")
            return

        parts = content.split()
        if len(parts) != 2:
            messagebox.showerror("Data Error", "Stored OTP data is corrupted or incomplete.")
            return

        saved_id, saved_otp = parts

        if entered_id == saved_id and entered_otp == saved_otp:
            messagebox.showinfo("Success", "OTP verified successfully.")
            root.destroy()
            showchangepasswordoption()
        else:
            messagebox.showwarning("Failed", "Incorrect OTP or User ID. Please try again.")

    heading = Label(root, text="Secure OTP Verification", font=("Segoe UI", 28, "bold"), fg="#0A3D62", bg="#f0f2f5")
    heading.place(x=300, y=50, anchor='center')

    Label(root, text='User ID:', font=("Segoe UI", 18), fg="#333333", bg="#f0f2f5").place(x=50, y=140)
    entry_login = Entry(root, width=30, font=('Segoe UI', 14), bg="#ffffff", fg="#333333")
    entry_login.place(x=200, y=145)

    Label(root, text='Enter OTP:', font=("Segoe UI", 18), fg="#333333", bg="#f0f2f5").place(x=50, y=200)
    entry_verify = Entry(root, width=30, font=('Segoe UI', 14), bg="#ffffff", fg="#333333")
    entry_verify.place(x=200, y=205)

    btn_send = Button(root, text='Send OTP', bg="#0f4c75", fg="white",
                      font=("Segoe UI", 8, "bold"), padx=10, pady=5,
                      cursor="hand2", command=send_otp)
    btn_send.place(x=510, y=145)

    btn_verify = Button(root, text='Verify OTP', bg="#0f4c75", fg="white",
                        font=("Segoe UI", 14, "bold"), padx=10, pady=5,
                        cursor="hand2", command=verify)
    btn_verify.place(x=300, y=320, anchor='center')
    
    show_var = IntVar()
    def toggle_otp():
        entry_verify.config(show='' if show_var.get() else '*')

    chk = Checkbutton(root, text="Show OTP", variable=show_var, command=toggle_otp,
                      font=("Segoe UI", 12), bg="#f0f2f5", activebackground="#f0f2f5")
    chk.place(x=200, y=240)
    
    def on_enter(e): btn_send['bg'] = '#3282b8'
    def on_leave(e): btn_send['bg'] = '#0f4c75'
    btn_send.bind("<Enter>", on_enter)
    btn_send.bind("<Leave>", on_leave)

    def on_enter2(e): btn_verify['bg'] = '#3282b8'
    def on_leave2(e): btn_verify['bg'] = '#0f4c75'
    btn_verify.bind("<Enter>", on_enter2)
    btn_verify.bind("<Leave>", on_leave2)

    root.mainloop()