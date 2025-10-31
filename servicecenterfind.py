import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showservicecenterfind():
    t=tkinter.Tk()
    t.geometry('1800x1200')
    t.title("Service Center Find")
    def cx():
        t.destroy()
    
    def finddata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        if not xa :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select name, address,email,phone,regno from servicecenter where officeid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e2.insert(0,str(res[0]))
        e3.insert(0,str(res[1]))
        e4.insert(0,str(res[2]))
        e5.insert(0,str(res[3]))
        e6.insert(0,str(res[4]))
        db.close()
    
    
    def clear():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select officeid  from servicecenter "
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close()    
         
    z=Label(t,text='Find in Service center', font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=450,y=50)    
        
    a=Label(t,text='Office ID :',font=('arial',15))
    a.place(x=350,y=150)
    e1=ttk.Combobox(t,font=('arial',17))
    filldata()
    e1.place(x=650,y=150)
         
    
    b=Label(t,text='Name:',font=('arial',15))
    b.place(x=350,y=270)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=650,y=270)
         
    
    c=Label(t,text='Address :',font=('arial',15))
    c.place(x=350,y=320)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=650,y=320)
         
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=350,y=370)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=650,y=370)
         
    
    e=Label(t,text='Phone :',font=('arial',15))
    e.place(x=350,y=420)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=650,y=420)
         
    
    
    f=Label(t,text='Registration no :',font=('arial',15))
    f.place(x=350,y=470)
    e6=Entry(t,width=25,font=('arial',15))
    e6.place(x=650,y=470)
    
        
        
    #Save Btn
    btn=Button(t,text='Back', bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn.place(x=750,y=550)
         
     #Close
    btn2=Button(t,text='Clear', bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=clear)
    btn2.place(x=450,y=550)
       #find
    btn3=Button(t,text='Find', bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 10, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=finddata)
    btn3.place(x=950,y=148)
           
    t.mainloop()