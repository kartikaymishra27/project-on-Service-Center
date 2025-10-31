import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showcustomerinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('Insert Customer')
    
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
        xg=e7.get()
        if not xa or not xb or not xc or not xd or not xe or not xf or not xg:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into customer values('%s','%s','%s','%s','%s','%s','%s')" %(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
      
        
        
    z=Label(t,text='Insert into Customer Details',font=('arial',20,'bold','underline'))
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
    c.place(x=100,y=320)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=320)
         
    
    d=Label(t,text='Email:',font=('arial',15))
    d.place(x=100,y=370)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=370)
         
    
    e=Label(t,text='Phone :',font=('arial',15))
    e.place(x=100,y=420)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=350,y=420)
         
    
    
    f=Label(t,text='Registration no :',font=('arial',15))
    f.place(x=100,y=470)
    e6=Entry(t,width=25,font=('arial',15))
    e6.place(x=350,y=470)
    
    g=Label(t,text='Product ID :',font=('arial',15))
    g.place(x=100,y=520)
    e7=Entry(t,width=25,font=('arial',15))
    e7.place(x=350,y=520)
         
    
        
        
    #Save Btn
    btn=Button(t,text='Save',font=('arial',20),bg='lightgray',fg='black',command=savedata)
    btn.place(x=150,y=600)
         
     #Close
    btn2=Button(t,text='Back',font=('arial',20),bg='lightgray',fg='black',command=cx)
    btn2.place(x=450,y=600)
    t.mainloop()