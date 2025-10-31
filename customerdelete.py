import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showcustomerdelete():
    t=tkinter.Tk()
    t.geometry('600x400')
    t.title('Delete Customer')
    t.configure(bg="#ECF0F1")
    
    def cx():
        t.destroy()
    
    def delete():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields.")
           return
        sql="delete from customer where cusid='%s'  "%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Delete')
        e1.delete(0,100)
        
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select cusid  from customer"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close()    
         
    
    
    
    z=Label(t,text='Delete from Customer',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=140,y=50)    
    
    a=Label(t,text='Customer id :',font=('arial',18))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',15))
    filldata()
    e1.place(x=250,y=150)
     
     
    #find
    btn1=Button(t,text='Delete',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=delete)
    btn1.place(x=150,y=250)
    
    btn2=Button(t,text='back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=350,y=250)
    t.mainloop()