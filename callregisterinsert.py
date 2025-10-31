import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql

def showcallregisterinsert():
    
    t=tkinter.Tk()
    t.geometry('900x800')
    t.title('Call Register Insert')
    t.configure(bg="#ECF0F1")
    def cx():
        t.destroy()
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select cusid  from customer"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e2['values']=lt
         
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
         e3['values']=lt
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
         e4['values']=lt         
         db.close() 
    def filldata3():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select engid from engineers"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e5['values']=lt
         db.close() 
    def checkdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur=db.cursor()
         xa=e1.get()
         sql="select count(*) from callregister where callid='%s'"%(xa)
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
        xf=int(e7.get())
        xg=e6.get()
        xh=e8.get()
        xi=e9.get()
        if not xa or not xb or not xc or not xd or not xe or not xf:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
      
        sql="insert into callregister values('%s','%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        sendemailcustomer()
        sendemailengineers()
        
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
        e9.delete(0,100)
        return True
    def finddata_callid_customerid():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e2.get()
        if not xa:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select  catid,productid from  customer where cusid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        
        e3.delete(0,100)
        e4.delete(0,100)
       
        e3.insert(0,str(res[0]))
        e4.insert(0,str(res[1]))
        
        db.close()
    def finddata_callid_engid():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         xa=e3.get()
         if not xa:
             messagebox.showwarning("Input Error", "Please fill all fields")
             return
         sql="select  engid from  engineers where catid='%s'"%(xa)
         cur.execute(sql)
         res=cur.fetchone()
         e5.delete(0,100)
         e5.insert(0,str(res[0]))
         
         
         db.close()
    def finddata_callid_sname():
           db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
           cur = db.cursor()
           xa=e3.get()
           xb=e4.get()
           if not xa and not xb:
               messagebox.showwarning("Input Error", "Please fill all fields")
               return
           sql="select  sname from  servicetypes where catid='%s' and productid='%s'"%(xa,xb)
           cur.execute(sql)
           res=cur.fetchone()
           e6.delete(0,100)
           e6.insert(0,str(res[0]))
           
           db.close()  
    def finddata_charges():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         xa=e3.get()
         xb=e4.get()
         xc=e6.get()
         if not xa and not xb and not xc:
             messagebox.showwarning("Input Error", "Please fill all fields")
             return
         sql="select  charges from  servicetypes where catid='%s' and productid='%s'and sname='%s'"%(xa,xb,xc)
         cur.execute(sql)
         res=cur.fetchone()
         e7.delete(0,100)
         e7.insert(0,str(res[0]))
         db.close()
    def finddata_cusid_email():
          db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
          cur = db.cursor()
          xa=e2.get()
          if not xa:
              messagebox.showwarning("Input Error", "Please fill all fields")
              return
          sql="select  email from  customer where cusid='%s'"%(xa)
          cur.execute(sql)
          res=cur.fetchone()
          e8.delete(0,100)
          e8.insert(0,str(res[0]))
    def finddata_engid_email():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         xa=e5.get()
         if not xa:
             messagebox.showwarning("Input Error", "Please fill all fields")
             return
         sql="select  email from  engineers where engid='%s'"%(xa)
         cur.execute(sql)
         res=cur.fetchone()
         e9.delete(0,100)
         e9.insert(0,str(res[0]))
      
    def combined_function():
        finddata_callid_customerid()
        finddata_callid_engid()
        finddata_callid_sname()
        finddata_charges()
        finddata_cusid_email()
        finddata_engid_email()
        filldatacusname()
        filldatacatname()
        filldataproductname()
        filldataename()
    def sendemailcustomer():
        from_address = "luckymishra741756@gmail.com"
        to_address = e8.get()

        msg = MIMEMultipart('alternative')
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Service Request Received"

        body = (
    f"Dear Valued Customer,\n\n"
    f"We sincerely thank you for reaching out to our Service Center.\n"
    f"Your service request has been successfully registered with the following details:\n\n"
    f"Call ID     : {e1.get()}\n"
    f"Service     : {e6.get()}\n"
    f"Charges     : ₹{e7.get()}\n\n"
    f"Assigned Engineer Email : {e9.get()}\n\n"
    f"Our team will be in touch with you shortly regarding further steps.\n"
    f"If you have any questions, feel free to contact us.\n\n"
    f"Warm regards,\n"
    f"Service Center Team"
)

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        username = 'luckymishra741756@gmail.com'
        password = 'nttxdlfyrcprgyce' 

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            messagebox.showinfo('Success', 'Mail sent to customer successfully.')
        except Exception as e:
            messagebox.showerror('Mail Error', f'Failed to send email:\n{str(e)}')

    def sendemailengineers():
       from_address = "luckymishra741756@gmail.com"
       to_address = e9.get()
   
       msg = MIMEMultipart('alternative')
       msg['From'] = from_address
       msg['To'] = to_address
       msg['Subject'] = "Engineers need for Service"
   
       # Correct MIMEText with 'plain' type
       part1 = MIMEText(
    f"Dear Engineer,\n\n"
    f"You have been assigned a new service request with the following details:\n\n"
    f"Call ID     : {e1.get()}\n"
    f"Customer ID : {e2.get()}\n"
    f"Customer Email : {e8.get()}\n"
    f"Category ID : {e3.get()}\n"
    f"Product ID  : {e4.get()}\n"
    f"Service     : {e6.get()}\n"
    f"Estimated Charge : ₹{e7.get()}\n\n"
    f"Please attend to this request at your earliest convenience to ensure timely service delivery.\n"
    f"For any queries or clarifications, contact the service manager.\n\n"
    f"Best regards,\n"
    f"Service Center Management"
, 'plain')

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
           messagebox.showinfo('Success', 'Mail sent  to engineers successfully.')
       except Exception as e:
           messagebox.showerror('Mail Error', f'Failed to send email:\n{str(e)}')
    def filldatacatname():
       db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
       cur = db.cursor()
       xa=e3.get()
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
       xa=e4.get()
       if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields")
           return
       sql="select  pname from products where productid='%s'"%(xa)
       cur.execute(sql)
       res=cur.fetchone()
       pname.delete(0,100)
       pname.insert(0,str(res[0]))

       db.close()
    def filldataename():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e5.get()
        if not xa :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select  ename from engineers where engid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        ename.delete(0,100)
        
        ename.insert(0,str(res[0]))
        
        db.close()
    
    def filldatacusname():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e2.get()
        if not xa :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select  cname from customer where cusid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        cusname.delete(0,100)
        cusname.insert(0,str(res[0]))

        db.close()
                  

    z=Label(t,text='Insert into callregister',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=230,y=50)    
        
    a=Label(t,text='Call ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Customer ID:',font=('arial',15))
    b.place(x=100,y=200)
    e2=ttk.Combobox(t,width=20,font=('arial',17))
    filldata()
    e2.place(x=350,y=200)
    e2.bind("<<ComboboxSelected>>", lambda event: filldatacusname())
    cusname= Entry(t, text='',font=('arial', 15), fg='blue')
    cusname.place(x=650, y=200)
    
    c=Label(t,text='Category ID:',font=('arial',15))
    c.place(x=100,y=250)
    e3=ttk.Combobox(t,width=20,font=('arial',17))
    filldata1()
    e3.place(x=350,y=250)
    e3.bind("<<ComboboxSelected>>", lambda event: filldatacatname())
    catname= Entry(t, text='',font=('arial', 15), fg='blue')
    catname.place(x=650, y=250)
    
    d=Label(t,text='Product ID:',font=('arial',15))
    d.place(x=100,y=300)
    e4=ttk.Combobox(t,width=20,font=('arial',17))
    filldata2()
    e4.place(x=350,y=300)
    e4.bind("<<ComboboxSelected>>", lambda event: filldataproductname())
    pname= Entry(t, text='',font=('arial', 15), fg='blue')
    pname.place(x=650, y=300)
    
    d=Label(t,text='Engineer ID:',font=('arial',15))
    d.place(x=100,y=350)
    e5=ttk.Combobox(t,width=20,font=('arial',17))
    filldata3()
    e5.place(x=350,y=350)
    e5.bind("<<ComboboxSelected>>", lambda event: filldataename())
    ename= Entry(t, text='',font=('arial', 15), fg='blue')
    ename.place(x=650, y=350)
    
    s=Label(t,text='Service Name:',font=('arial',15))
    s.place(x=100,y=400)
    e6=Entry(t,width=25,font=('arial',15))
    e6.place(x=350,y=400)
    
    e=Label(t,text='Estimash Charge:',font=('arial',15))
    e.place(x=100,y=450)
    e7=Entry(t,width=25,font=('arial',15))
    e7.place(x=350,y=450)
    
     
    f=Label(t,text='Email(Customer):',font=('arial',15))
    f.place(x=100,y=500)
    e8=Entry(t,width=25,font=('arial',15))
    e8.place(x=350,y=500)

    g=Label(t,text='Email(Engineer):',font=('arial',15))
    g.place(x=100,y=550)
    e9=Entry(t,width=25,font=('arial',15))
    e9.place(x=350,y=550)
    
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=590)
     
    #Save Btn
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=590)

    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    btn3=Button(t,text=' Find  ',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=combined_function)
    btn3.place(x=720,y=148)
    
    t.mainloop()