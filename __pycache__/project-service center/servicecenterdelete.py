import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showservicecenterdelete():
    t=tkinter.Tk()
    t.geometry('600x400')
    t.title("Service Center delete")
    def cx():
        t.destroy()
    
    def delete():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        if not xa or not xb:
           messagebox.showwarning("Input Error", "Please fill all fields.")
           return
        sql="delete from servicecenter where officeid='%s' and name='%s' "%(xa,xb)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Delete')
        e1.delete(0,100)
        e2.delete(0,100)
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
         
    
    
    
    z=Label(t,text='Delete from Service center',font=('arial',20,'bold','underline'))
    z.place(x=140,y=50)    
    
    a=Label(t,text='Office id :',font=('arial',20))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',15))
    filldata()
    e1.place(x=250,y=150)
     
    b=Label(t,text='Name :',font=('arial',20))
    b.place(x=100,y=210)
    e2=Entry(t,width=20,font=('arial',16))
    e2.place(x=250,y=210)
     
     
     
    #find
    btn1=Button(t,text='Delete',font=('arial',18),bg='lightGray',command=delete)
    btn1.place(x=100,y=290)
    
    btn2=Button(t,text='back',font=('arial',18),bg='lightgray',fg='black',command=cx)
    btn2.place(x=400,y=290)
    t.mainloop()