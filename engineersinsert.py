import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
def showengineersinsert():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("Engineers insert")
    
    def cx():
        t.destroy()
    def filldata1():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        sql="select catid from productcategory"
        lt=[]
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(str(res[0]))
        e6['values']=lt
        db.close() 
    def sendemailengineers():
        from_address = "luckymishra741756@gmail.com"
        to_address = e4.get()
    
        msg = MIMEMultipart('alternative')
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Engineers need for Service"
    
        # Correct MIMEText with 'plain' type
        part1 = MIMEText(f'''
Dear {e2.get()},

We are pleased to inform you that a new service task has been assigned to you in the system.

Details:
• Engineer ID     : {e1.get()}
• Name            : {e2.get()}
• Category ID     : {e6.get()}
• Category Name   : {catname.get()}


Please log in to the Service Center Management System to view and accept the task. Your timely response is crucial to maintaining our service standards.

If you have any questions, please reach out to your supervisor or the support team.

Best regards,  
Service Center Management Team
''', 'plain')
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
    
    def savedata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        if not xa or not xb or not xc or not xd or not xe or not xf:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        if not xe.isdigit() or len(xe) != 10:
            messagebox.showinfo("Invalid", "Phone number must be exactly 10 digits and only numbers")
            return
        sql="insert into engineers values('%s','%s','%s','%s','%s','%s')" %(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        sendemailengineers()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        xa=e1.get()
        sql="select count(*) from engineers where engid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('hi','ID Available')
        else:
            messagebox.showinfo('not  available','ID already Exist')
            db.close()  
    def filldatacatname():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         xa=e6.get()
         if not xa :
             messagebox.showwarning("Input Error", "Please fill all fields")
             return
         sql="select  catname from productcategory where catid='%s'"%(xa)
         cur.execute(sql)
         res=cur.fetchone()
         catname.delete(0,100)
         
         catname.insert(0,str(res[0]))
         
         db.close()
        
    z=Label(t,text='Insert into Engineer',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=370,y=50,anchor='center')    
        
    a=Label(t,text='Engineer ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Engineer Name:',font=('arial',15))
    b.place(x=100,y=200)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=200)
         
    c=Label(t,text='Address :',font=('arial',15))
    c.place(x=100,y=250)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=250)
         
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=100,y=300)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=300)
         
    
    e=Label(t,text='Phone :',font=('arial',15))
    e.place(x=100,y=350)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=350,y=350)
         
    
    
    f=Label(t,text='Category ID:',font=('arial',15))
    f.place(x=100,y=400)
    e6=ttk.Combobox(t,width=20,font=('arial',17))
    filldata1()
    e6.place(x=350,y=400)
    e6.bind("<<ComboboxSelected>>", lambda event: filldatacatname())
    
    catname = Label(t, text='Category Name:', font=('arial', 15))
    catname.place(x=100, y=450)
    catname = Entry(t, text='', font=('arial', 15), fg='blue')
    catname.place(x=350, y=450)
         
    
        
        
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
    
    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    
    
    t.mainloop()