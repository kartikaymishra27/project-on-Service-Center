import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showstaffinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    
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
        if not xa or not xb or not xc or not xd or not xe:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into staff values('%s','%s','%s','%s',%s)"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
      
        
        
    z=Label(t,text='Insert into staff',font=('arial',20,'bold','underline'))
    z.place(x=180,y=50)    
        
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
    btn=Button(t,text='Save',font=('arial',20),bg='lightgray',fg='black',command=savedata)
    btn.place(x=150,y=500)
         
     #Close
    btn2=Button(t,text='Back',font=('arial',20),bg='lightgray',fg='black',command=cx)
    btn2.place(x=450,y=500)
    t.mainloop()