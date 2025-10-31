import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
def showcustomerinsert():
    t=tkinter.Tk()
    t.geometry('800x700')
    t.title('Insert Customer')
    t.configure(bg="#ECF0F1")
    
    def cx():
        t.destroy()
    def checkdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur=db.cursor()
         xa=e1.get()
         sql="select count(*) from customer where cusid='%s'"%(xa)
         cur.execute(sql)
         data=cur.fetchone()
         if data[0]==0:
             messagebox.showinfo('hi','ID Available')
         else:
             messagebox.showinfo('not  available','ID already Exist')
             db.close()
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
    def filldata2():
          db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
          cur = db.cursor()
          sql="select productid  from products"
          lt=[]
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(str(res[0]))
          e7['values']=lt         
          db.close() 
    def savedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        xa = e1.get()
        xb = e2.get()
        xc = e3.get()
        xd = em.get()
        xe = e5.get()
        xf = e6.get()
        xg = e7.get()
    
        if not xa or not xb or not xc or not xd or not xe or not xf or not xg:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return False
        if not xe.isdigit() or len(xe) != 10:
            messagebox.showinfo("Invalid", "Phone number must be exactly 10 digits and only numbers")
            return False
    
        sql = "insert into customer values('%s','%s','%s','%s','%s','%s','%s')" % (xa, xb, xc, xd, xe, xf, xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Saved', 'Your data is saved successfully.')
        sendemailcustomer()
        # Clear fields
        e1.delete(0, 100)
        e2.delete(0, 100)
        e3.delete(0, 100)
        em.delete(0, 100)
        e5.delete(0, 100)
        e6.delete(0, 100)
        e7.delete(0, 100)
        
        return True
    def sendemailcustomer():
        from_address = "luckymishra741756@gmail.com"
        to_address = em.get()
        cname = e2.get()
        msg = MIMEMultipart('alternative')
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Service Request Received"
    
        body = f'''Dear {cname},
Thank you for reaching out to us.

We are pleased to inform you that your service request has been successfully received and is now being processed. Our support team will handle your request with utmost priority and ensure that you are kept informed throughout the process.

Should you have any further questions or require additional assistance, please do not hesitate to contact us.

The Estimash charges will be send to you soon regarding services.s

Best regards,  
Service Center Team'''

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
    
    def filldataproductname():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e7.get()
        if not xa :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select  pname from products where productid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        productname_value.delete(0,100)
        productname_value.insert(0,str(res[0]))

        db.close()
         
    
    z=Label(t,text='Insert into Customer Details',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=180,y=50)    
        
    a=Label(t,text='Customer ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Customer Name:',font=('arial',15))
    b.place(x=100,y=220)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=220)
         
    
    c=Label(t,text='Address :',font=('arial',15))
    c.place(x=100,y=270)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=270)
         
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=100,y=320)
    em=Entry(t,width=25,font=('arial',15))
    em.place(x=350,y=320)
   
   
         
    
    e=Label(t,text='Phone :',font=('arial',15))
    e.place(x=100,y=370)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=350,y=370)
         
    
    
    f=Label(t,text='Category ID :',font=('arial',15))
    f.place(x=100,y=420)
    e6=ttk.Combobox(t,width=20,font=('arial',17))
    filldata1()
    e6.place(x=350,y=420)
    e6.bind("<<ComboboxSelected>>", lambda event: filldatacatname())

    
    catname = Label(t, text='Category Name:', font=('arial', 15))
    catname.place(x=100, y=460)
    catname = Entry(t, text='', font=('arial', 15), fg='blue')
    catname.place(x=350, y=460)
    
    g=Label(t,text='Product ID :',font=('arial',15))
    g.place(x=100,y=500)
    e7=ttk.Combobox(t,width=20,font=('arial',17))
    filldata2()
    e7.place(x=350,y=500)
    e7.bind("<<ComboboxSelected>>", lambda event: filldataproductname())
    
         
    productname_label = Label(t, text='Product Name:', font=('arial', 15))
    productname_label.place(x=100, y=540)
    productname_value = Entry(t, text='', font=('arial', 15), fg='blue')
    productname_value.place(x=350, y=540)
         
    
        
        
    #Save Btn
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=580)
         
     #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=580)
    
    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    t.mainloop()