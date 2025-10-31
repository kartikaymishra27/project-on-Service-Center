import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
def showstaffinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title("Staff insert")
    t.configure(bg="#ECF0F1")
    
    def cx():
        t.destroy()
    def sendemail():
         from_address = "luckymishra741756@gmail.com"
         to_address = e4.get()
         sname = e2.get()
        
         msg = MIMEMultipart('alternative')
         msg['From'] = from_address
         msg['To'] = to_address
         msg['Subject'] = "Staff nedds for Services"
     
         part1 = MIMEText(
    '''Dear Staff Member({sname}),

You have been assigned a new service task as part of your responsibilities at our Service Center.

A customer is in need of technical assistance, and engineers have been allocated accordingly to handle the issue efficiently.

Please review the assignment and confirm your availability at the earliest.

Thank you for your continued support and commitment.

Best regards,  
Service Center Management
''', 'plain')

         part1 = MIMEText(body, 'plain')
         msg.attach(part1)
     
         username = 'luckymishra741756@gmail.com'
         password = 'nttx dlfy rcpr gyce'  
     
         try:
             server = smtplib.SMTP('smtp.gmail.com', 587)
             server.ehlo()
             server.starttls()
             server.login(username, password)
             server.sendmail(from_address, to_address, msg.as_string())
             server.quit()
             messagebox.showinfo('Success', 'Mail sent successfully.')
         except Exception as e:
             messagebox.showerror('Mail Error', f'Failed to send email:\n{str(e)}')
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        xa=e1.get()
        sql="select count(*) from staff where staffid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('hi','ID Available')
        else:
            messagebox.showinfo('not  available','ID already Exist')
            db.close()
    def savedata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        if not xa or not xb or not xc or not xd or not xe:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        if not xe.isdigit() or len(xe) != 10:
            messagebox.showinfo("Invalid", "Phone number must be exactly 10 digits and only numbers")
            return
        sql="insert into staff values('%s','%s','%s','%s',%s)"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        sendemail()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
   
                
    z=Label(t,text='Insert into staff',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=300,y=50)    
        
    a=Label(t,text='Staffid :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Staff name:',font=('arial',15))
    b.place(x=100,y=220)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=220)
         
    
    c=Label(t,text='Address:',font=('arial',15))
    c.place(x=100,y=290)
    e3=Entry(t,width=25,font=('arial',15))
    e3.place(x=350,y=290)
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=100,y=360)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=360)
    
    d=Label(t,text='Phone:',font=('arial',15))
    d.place(x=100,y=430)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=350,y=430)
         
         
    #Save Btn
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=500)
         
     #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=500)
    
    btn3=Button(t,text='check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    
    t.mainloop()