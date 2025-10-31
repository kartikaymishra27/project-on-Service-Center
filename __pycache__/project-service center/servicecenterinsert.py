import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showservicecenterinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title("Service center insert")
    def cx():
        t.destroy()
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
        sql="insert into servicecenter values('%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        
    z=Label(t,text='Insert into Service center',font=('arial',20,'bold','underline'))
    z.place(x=180,y=50)    
        
    a=Label(t,text='Office ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Name:',font=('arial',15))
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
         
    
    
    f=Label(t,text='Registration no :',font=('arial',15))
    f.place(x=100,y=400)
    e6=Entry(t,width=25,font=('arial',15))
    e6.place(x=350,y=400)
    
        
        
    #Save Btn
    btn=Button(t,text='Save',font=('arial',20),bg='lightgray',fg='black',command=savedata)
    btn.place(x=150,y=500)
         
     #Close
    btn2=Button(t,text='Back',font=('arial',20),bg='lightgray',fg='black',command=cx)
    btn2.place(x=450,y=500)
    
    
    
    t.mainloop()