import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showproductcategoryinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title("Product Category Insert")
    def cx():
        t.destroy()
    def savedata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        if not xa or not xb or not xc:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into productcategory values('%s','%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
      
        
        
    z=Label(t,text='Insert into Product category',font=('arial',20,'bold','underline'))
    z.place(x=180,y=50)    
        
    a=Label(t,text='Category ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Category Name:',font=('arial',15))
    b.place(x=100,y=220)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=220)
         
    
    c=Label(t,text='Description :',font=('arial',15))
    c.place(x=100,y=290)
    e3=Entry(t,width=25,font=('arial',15))
    e3.place(x=350,y=290)
         
    
        
        
    #Save Btn
    btn=Button(t,text='Save',font=('arial',20),bg='lightgray',fg='black',command=savedata)
    btn.place(x=150,y=400)
         
     #Close
    btn2=Button(t,text='Back',font=('arial',20),bg='lightgray',fg='black',command=cx)
    btn2.place(x=450,y=400)
    t.mainloop()