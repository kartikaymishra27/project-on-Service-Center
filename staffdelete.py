import tkinter
import pymysql
import smtplib
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
def showstaffdelete():
    t=tkinter.Tk()
    t.geometry('600x400')
    t.title('Staff delete')
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
        sql="delete from staff where staffid='%s'  "%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Delete')
        e1.delete(0,100)
        
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select staffid  from staff"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close()    
         
    
    
    
    z=Label(t,text='Delete from staff',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=300,y=50,anchor='center')    
    
    a=Label(t,text='Staff id:',font=('arial',18))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,font=('arial',15))
    filldata()
    e1.place(x=250,y=150)
     
     
    #find
    btn1=Button(t,text='Delete',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=delete)
    btn1.place(x=100,y=250)
    
    #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=400,y=250)
    t.mainloop()
