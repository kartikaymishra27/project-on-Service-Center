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
    def checkdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur=db.cursor()
         xa=e1.get()
         sql="select count(*) from productcategory where catid='%s'"%(xa)
         cur.execute(sql)
         data=cur.fetchone()
         if data[0]==0:
             messagebox.showinfo('hi','ID Available')
         else:
             messagebox.showinfo('not  available','ID already Exist')
             db.close()    
      
        
        
    z=Label(t,text='Insert into Product category', font=("Segoe UI", 24, "bold"), fg="#0A3D62",
            bg="white", relief="raised")
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
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=400)
         
     #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=400)
    
    btn3=Button(t,text='check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    t.mainloop()
