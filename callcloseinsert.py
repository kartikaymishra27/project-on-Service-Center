import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

def showcallcloseinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('Call Close Insert')
    t.configure(bg="#ECF0F1")
    def cx():
        t.destroy()
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select callid from callregister"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close() 
    def filldata1():
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
    def filldata2():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select engid from engineers"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e3['values']=lt
         db.close() 
    def delete():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
      
        if not xa:
           messagebox.showwarning("Input Error", "Please fill all fields.")
           return
        sql="delete from callregister where callid='%s'"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Successfukky Deleted from callregister')
        e1.delete(0,100)
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        xa=e1.get()
        
        sql="select count(*) from callclose where callid='%s' "%(xa)
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
        if not xa or not xb or not xc or not xd :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into callclose values('%s','%s','%s','%s')"%(xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        delete()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    def filldatacatname():
       db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
       cur = db.cursor()
       xa=e2.get()
       if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields")
           return
       sql="select  cname from customer where cusid='%s'"%(xa)
       cur.execute(sql)
       res=cur.fetchone()
       cname.delete(0,100)
       cname.insert(0,str(res[0]))
       
       db.close()
   
    def filldatapname():
       db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
       cur = db.cursor()
       xa=e3.get()
       if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields")
           return
       sql="select  ename from engineers  where engid='%s'"%(xa)
       cur.execute(sql)
       res=cur.fetchone()
       pname.delete(0,100)
       pname.insert(0,str(res[0]))

       db.close()
   
        
    z=Label(t,text='Insert into Call Close',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=350,y=50,anchor='center')    
        
    a=Label(t,text='Call ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20,font=('arial',17))
    filldata()
    e1.place(x=350,y=150)
    
    
    b=Label(t,text='Customer ID:',font=('arial',15))
    b.place(x=100,y=200)
    e2=ttk.Combobox(t,width=20,font=('arial',17))
    filldata1()
    e2.place(x=350,y=200)
    e2.bind("<<ComboboxSelected>>", lambda event: filldatacatname())
    
    cname = Label(t, text='Customer Name:', font=('arial', 15))
    cname.place(x=100, y=240)
    cname = Entry(t, text='', font=('arial', 15), fg='blue')
    cname.place(x=350, y=240)
         
    
    c=Label(t,text='Engineer ID :',font=('arial',15))
    c.place(x=100,y=290)
    e3=ttk.Combobox(t,width=20,font=('arial',17))
    filldata2()    
    e3.place(x=350,y=290)
    e3.bind("<<ComboboxSelected>>", lambda event: filldatapname())
    
    pname = Label(t, text='Engineer Name:', font=('arial', 15))
    pname.place(x=100, y=330)
    pname = Entry(t, text='', font=('arial', 15), fg='blue')
    pname.place(x=350, y=330)
         
         
    
    d=Label(t,text='Date Of Close:',font=('arial',15))
    d.place(x=100,y=380)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=380)
    e4.insert(0, datetime.now().strftime("%d/%m/%Y"))
         
    
        
    #Save Btn
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=430)
         
    #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=430)
    
    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)    
    t.mainloop()