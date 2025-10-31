import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showproductcategoryfind():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title("Product category Find")
    def cx():
        t.destroy()
    
    def finddata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        if not xa :
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="select catname ,description from productcategory where catid='%s'"%(xa)
        cur.execute(sql)
        res=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
       
        e2.insert(0,str(res[0]))
        e3.insert(0,str(res[1]))
       
        db.close()
    
    
    def clear():
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select catid  from productcategory "
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close()    
         
    z=Label(t,text='Find in Product Category',font=('arial',20,'bold','underline'))
    z.place(x=250,y=50)    
        
    a=Label(t,text='Category ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',17))
    filldata()
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Category Name:',font=('arial',15))
    b.place(x=100,y=220)
    e2=Entry(t,width=25,font=('arial',15))
    e2.place(x=350,y=220)
         
    
    c=Label(t,text='Description :',font=('arial',15))
    c.place(x=100,y=270)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=270)
         
    
    
        
        
    #Save Btn
    btn=Button(t,text='Back',font=('arial',15),bg='lightgray',fg='black',command=cx)
    btn.place(x=450,y=400)
         
     #Close
    btn2=Button(t,text='Clear',font=('arial',15),bg='lightgray',fg='black',command=clear)
    btn2.place(x=250,y=400)
       #find
    btn3=Button(t,text='Find',font=('arial',12),bg='lightGray',command=finddata)
    btn3.place(x=645,y=148)
    
    
    
    t.mainloop()