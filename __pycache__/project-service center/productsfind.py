import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showproductfind():
    t=tkinter.Tk()
    t.geometry('800x700')
    t.title('Product Find')
    def cx():
        t.destroy()
    
    def finddata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        if not xa:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select productid,pname,catid,warrantydays from products where productid='%s'"%(xa)
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
         sql="select productid  from products "
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close()    
         
    z=Label(t,text='Find in Products',font=('arial',20,'bold','underline'),bg='white')
    z.place(x=280,y=50)    
        
    a=Label(t,text='Product ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',17))
    filldata()
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Product Name:',font=('arial',15))
    b.place(x=100,y=270)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=270)
         
    
    c=Label(t,text='Catagory ID:',font=('arial',15))
    c.place(x=100,y=320)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=320)
         
    
    d=Label(t,text='Warranty Days:',font=('arial',15))
    d.place(x=100,y=370)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=370)
      
    
    #Reset Btn
    btn=Button(t,text='Back',font=('arial',15),bg='lightgray',fg='black',command=cx)
    btn.place(x=450,y=550)
         
    #Close
    btn2=Button(t,text='Clear',font=('arial',15),bg='lightgray',fg='black',command=clear)
    btn2.place(x=250,y=550)
    
    #find
    btn3=Button(t,text='Find',font=('arial',12),bg='lightgray',command=finddata)
    btn3.place(x=645,y=148)
    
    t.mainloop()