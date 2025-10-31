import tkinter 
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loginotpverify import showotpverify
import random

def showotpsend():
    t = tkinter.Tk()
    t.geometry('600x400')
    t.title('OTP Send')
    
    def sendgmail():
        from_address = "luckymishra741756@gmail.com"
        to_address = e1.get()
        
        if not to_address:
            messagebox.showwarning("Input Required", "Please enter your email address before proceeding.")
            return 
    
        if "@" not in to_address or "." not in to_address:
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            return 
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Secure OTP for Your Authorized Access - Service Center"
        msg['From'] = from_address
        msg['To'] = to_address
        
        r = random.randint(100000, 999999)
        
        html = f"""
        <html>
          <body style="font-family: 'Segoe UI', sans-serif; background-color: #f4f6f7; color: #2c3e50;">
            <div style="padding: 25px; border: 1px solid #dcdde1; border-radius: 10px; background-color: #ffffff; max-width: 650px; margin: auto;">
              <h2 style="color: #1e3799; text-align: center;">OTP for Authorized Account Verification</h2>
              
              <p>Dear Authorized User,</p>

              <p>
                You have requested secure access to your Service Center account. To proceed, please use the One-Time Password (OTP) provided below to verify your identity.
              </p>

              <p style="font-size: 26px; font-weight: bold; color: #e74c3c; text-align: center;">
                {r}
              </p>

              <p>
                This OTP is valid for a limited time and can only be used once. For your protection, please do not share this code with anyone.
              </p>

              <p>
                If you initiated this action, you may now continue the login or reset process. If this request was not made by you, please report it immediately to our support team.
              </p>

              <hr style="border-top: 1px solid #bdc3c7;">

              <p style="font-size: 14px;">
                🔒 Need help or want to report an issue?<br>
                Contact our team directly at: <strong>luckymishra741756@gmail.com</strong>
              </p>

              <p>
                Thank you for trusting Service Center. Your account security is our top priority.
              </p>

              <p>
                Sincerely,<br>
                <strong>Service Center Support Team</strong><br>
                Empowering secure digital solutions.
              </p>
            </div>
          </body>
        </html>
        """
            
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
    
        username = 'luckymishra741756@gmail.com'  
        password = 'nttx dlfy rcpr gyce'

        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username, password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()

        messagebox.showinfo('Email Sent', 'The OTP has been successfully sent to the registered email.')
        
        f = open('myotpproject.txt', 'w')
        f.write(to_address + ' ')
        f.write(str(r))
        f.close()

        messagebox.showinfo('Success', 'OTP details have been saved successfully.')
        t.destroy()
        showotpverify(to_address)

    title = Label(t, text="Send OTP", font=("Segoe UI", 32, "bold"), fg="#0A3D62", bg="white", relief="raised")
    title.place(x=300, y=50, anchor='center')

    a = Label(t, text='Email:', font=("Segoe UI", 28), fg="#333333", bg="#f0f2f5")
    a.place(x=50, y=157)

    e1 = Entry(t, width=30, font=('Segoe UI', 17), bg="#f5f5f5", fg="#333333")
    e1.place(x=200, y=170)

    btn1 = Button(t, text='Send OTP', bg="#0f4c75", fg="white", relief="raised",
                  font=("Segoe UI", 15, "bold"), padx=10, pady=5,
                  cursor="hand2", command=sendgmail)
    btn1.place(x=300, y=260, anchor='center')

    def on_enter(e): btn1['bg'] = '#3282b8'
    def on_leave(e): btn1['bg'] = '#0f4c75'
    btn1.bind("<Enter>", on_enter)
    btn1.bind("<Leave>", on_leave)

    t.mainloop()
