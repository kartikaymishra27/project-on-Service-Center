import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showcallcloseinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('Call Close Insert')
    def cx():
        t.destroy()
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
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        
    z=Label(t,text='Insert into Call Close',font=('arial',20,'bold','underline'))
    z.place(x=180,y=50)    
        
    a=Label(t,text='Call ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Customer ID:',font=('arial',15))
    b.place(x=100,y=200)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=200)
         
    
    c=Label(t,text='Engineer ID :',font=('arial',15))
    c.place(x=100,y=250)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=250)
         
    
    d=Label(t,text='Date Of Close:',font=('arial',15))
    d.place(x=100,y=300)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=300)
         
    
        
    #Save Btn
    btn=Button(t,text='Save',font=('arial',20),bg='lightgray',fg='black',command=savedata)
    btn.place(x=150,y=400)
         
    #Close
    btn2=Button(t,text='Back',font=('arial',20),bg='lightgray',fg='black',command=cx)
    btn2.place(x=450,y=400)
    
    
    
    t.mainloop()