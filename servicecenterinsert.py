import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql

def showservicecenterinsert():
    t = tkinter.Tk()
    t.geometry('1800x1200')
    t.title("Service Center Insert")
    t.configure(bg='white')

    def cx():
        t.destroy()

    def checkdata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        xa = e1.get()
        sql = "SELECT COUNT(*) FROM servicecenter WHERE officeid='%s'" % (xa)
        cur.execute(sql)
        data = cur.fetchone()
        if data[0] == 0:
            messagebox.showinfo('Available', 'ID is Available')
        else:
            messagebox.showinfo('Not Available', 'ID already exists')
        db.close()

    def savedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        xa = e1.get()
        xb = e2.get()
        xc = e3.get()
        xd = e4.get()
        xe = e5.get()
        xf = e6.get()

        if len(xa) == 0 or len(xb) == 0 or len(xc) == 0 or len(xd) == 0 or len(xe) == 0 or len(xf) == 0:
            messagebox.showinfo('Input Error', 'Please fill all fields')
            return

        if not xe.isdigit() or len(xe) != 10:
            messagebox.showinfo("Invalid", "Phone number must be exactly 10 digits and numeric")
            return
        else:
            sql = "INSERT INTO servicecenter VALUES('%s','%s','%s','%s','%s','%s')" % (xa, xb, xc, xd, xe, xf)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Success', 'Your data has been saved')
            sendemailcustomer()
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)

    def sendemailcustomer():
        from_address = "luckymishra741756@gmail.com"
        to_address = e4.get()

        msg = MIMEMultipart('alternative')
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Service Center Registration Confirmation"

        part1 = MIMEText(
f'''Dear Customer ({e2.get()}),

Thank you for registering your service request with us.

Your details have been successfully recorded as follows:
• Office ID       : {e1.get()}
• Name            : {e2.get()}
• Registration No.: {e6.get()}

Our team will begin processing your request, and we’ll keep you informed about the progress. If you need any assistance, feel free to contact us.

Thank you for choosing our Service Center.

Warm regards,  
Service Center Management Team
''', 'plain')
        msg.attach(part1)

        username = 'luckymishra741756@gmail.com'
        password = 'nttx dlfy rcpr gyce'  # Use app password

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            messagebox.showinfo('Success', 'Email sent successfully.')
        except Exception as e:
            messagebox.showerror('Mail Error', f'Failed to send email:\n{str(e)}')

    # Title
    z = Label(t, text='Insert into Service Center', font=("Segoe UI", 24, "bold"),
              fg="#0A3D62", bg="white", relief="raised")
    z.place(x=450, y=50)

    # Labels and Entries (Centered)
    a = Label(t, text='Office ID:', font=('arial', 15), bg='white')
    a.place(x=350, y=150)
    e1 = Entry(t, width=25, font=('arial', 15))
    e1.place(x=650, y=150)

    b = Label(t, text='Name:', font=('arial', 15), bg='white')
    b.place(x=350, y=200)
    e2 = Entry(t, width=25, font=('arial', 15))
    e2.place(x=650, y=200)

    c = Label(t, text='Address:', font=('arial', 15), bg='white')
    c.place(x=350, y=250)
    e3 = Entry(t, width=25, font=('arial', 15))
    e3.place(x=650, y=250)

    d = Label(t, text='Email:', font=('arial', 15), bg='white')
    d.place(x=350, y=300)
    e4 = Entry(t, width=25, font=('arial', 15))
    e4.place(x=650, y=300)

    e = Label(t, text='Phone:', font=('arial', 15), bg='white')
    e.place(x=350, y=350)
    e5 = Entry(t, width=25, font=('arial', 15))
    e5.place(x=650, y=350)

    f = Label(t, text='Registration No:', font=('arial', 15), bg='white')
    f.place(x=350, y=400)
    e6 = Entry(t, width=25, font=('arial', 15))
    e6.place(x=650, y=400)

    # Buttons
    btn = Button(t, text='Save', bg="#0f4c75", fg="white", width=6,
                 font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                 cursor="hand2", command=savedata)
    btn.place(x=400, y=500)

    btn2 = Button(t, text='Back', bg="#0f4c75", fg="white", width=6,
                  font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                  cursor="hand2", command=cx)
    btn2.place(x=700, y=500)

    btn3 = Button(t, text='Check', bg="#0f4c75", fg="white", width=5,
                  font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                  cursor="hand2", command=checkdata)
    btn3.place(x=950, y=148)

    t.mainloop()