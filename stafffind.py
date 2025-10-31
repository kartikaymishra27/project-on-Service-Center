import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showstafffind():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("Staff Find")
    t.configure(bg="#ECF0F1")
    def cx():
        t.destroy()
    
    def finddata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        if not xa:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select sname, address,email,phone from staff where staffid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
       
        e2.insert(0,str(res[0]))
        e3.insert(0,str(res[1]))
        e4.insert(0,str(res[2]))
        e5.insert(0,str(res[3]))
        
        db.close()
    
    
    
    def clear():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select staffid from staff"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         
         db.close()    
    
    z=Label(t,text='Find in staff',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=300,y=50)  
         
    
        
    a=Label(t,text='Staff Id:',font=('arial',15))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',17))
    filldata()
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Stff name:',font=('arial',15))
    b.place(x=100,y=220)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=220)
         
    
    c=Label(t,text='Address:',font=('arial',15))
    c.place(x=100,y=270)
    e3=Entry(t,width=25,font=('arial',15))
    e3.place(x=350,y=270)
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=100,y=310)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=310)
    
    e=Label(t,text='Phone:',font=('arial',15))
    e.place(x=100,y=360)
    e5=Entry(t,width=25,font=('arial',15))
    
    e5.place(x=350,y=360)
        
    btn=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn.place(x=450,y=400)
         
     #Close
    btn2=Button(t,text='Clear',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=clear)
    btn2.place(x=250,y=400)
       #find
    btn3=Button(t,text='Find',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=finddata)
    btn3.place(x=645,y=148)
    
    
    
    t.mainloop()
