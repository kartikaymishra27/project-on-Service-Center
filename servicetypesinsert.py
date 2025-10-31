import pymysql
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def showservicetypesinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('Servicetypes Insert')
    def cx():
        t.destroy()
    def filldata1():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        sql="select catid from productcategory"
        lt=[]
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(str(res[0]))
        e2['values']=lt
        db.close() 
    def filldata2():
          db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
          cur = db.cursor()
          sql="select productid  from products"
          lt=[]
          cur.execute(sql)
          data=cur.fetchall()
          for res in data:
              lt.append(str(res[0]))
          e3['values']=lt         
          db.close()
    def savedata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        if not xa or not xb or not xc or not xd or not xe or not xf:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into servicetype values('%s','%s','%s','%s','%d','%s')"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
       
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur=db.cursor()
        xa=e1.get()
        sql="select count(*) from servicetypes where serviceid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('hi','ID Available')
        else:
            messagebox.showinfo('not available',' ID already exist')
            db.close()
    def filldatacatname():
       db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
       cur = db.cursor()
       xa=e2.get()
       if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields")
           return
       sql="select  catname from productcategory where catid='%s'"%(xa)
       cur.execute(sql)
       res=cur.fetchone()
       catname.delete(0,100)
       
       catname.insert(0,str(res[0]))
       
       db.close()
   
    def filldataproductname():
       db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
       cur = db.cursor()
       xa=e3.get()
       if not xa :
           messagebox.showwarning("Input Error", "Please fill all fields")
           return
       sql="select  pname from products where productid='%s'"%(xa)
       cur.execute(sql)
       res=cur.fetchone()
       productname_value.delete(0,100)
       productname_value.insert(0,str(res[0]))

       db.close()
        
    z=Label(t,text='Insert into Service Type',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=180,y=50)    
        
    a=Label(t,text='Service ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=Entry(t,width=25,font=('arial',15))
    e1.place(x=350,y=150)
    
         
    
    b=Label(t,text='Catagory ID :',font=('arial',15)) 
    b.place(x=100,y=200)
    e2=ttk.Combobox(t,width=20,font=('arial',17))
    filldata1()
    
    e2.place(x=350,y=200)
    e2.bind("<<ComboboxSelected>>", lambda event: filldatacatname())

    
    catname = Label(t, text='Category Name:', font=('arial', 15))
    catname.place(x=100, y=250)
    catname = Entry(t, text='', font=('arial', 15), fg='blue')
    catname.place(x=350, y=250)



    c=Label(t,text='Product ID:',font=('arial',15))
    c.place(x=100,y=290)
    e3=ttk.Combobox(t,width=20,font=('arial',17))
    filldata2()
    e3.place(x=350,y=290)
    e3.bind("<<ComboboxSelected>>", lambda event: filldataproductname())
    
         
    productname_label = Label(t, text='Product Name:', font=('arial', 15))
    productname_label.place(x=100, y=340)
    productname_value = Entry(t, text='', font=('arial', 15), fg='blue')
    productname_value.place(x=350, y=340)
    
    d=Label(t,text='Service Name',font=('arial',15))
    d.place(x=100,y=380)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=380)
    
    e=Label(t,text='Charges',font=('arial',15))
    e.place(x=100,y=420)
    e5=Entry(t,width=25,font=('arial',15))
    e5.place(x=350,y=420)
    
    f=Label(t,text='Estimation Time',font=('arial',15))
    f.place(x=100,y=460)
    e6=Entry(t,width=25,font=('arial',15))
    e6.place(x=350,y=460)
         
    #Save Btn
    btn=Button(t,text='Save',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=savedata)
    btn.place(x=150,y=500)
         
     #Close
    btn2=Button(t,text='Back',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 14, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=cx)
    btn2.place(x=450,y=500)
    
    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    
    t.mainloop()