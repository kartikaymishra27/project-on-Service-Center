import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql

def showcallfeedbackinsert():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('Call feedback insert')
    t.configure(bg="#ECF0F1")
    
    def cx():
        t.destroy()
    def filldata():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         sql="select callid from callregister"
         lt=[]
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             lt.append(str(res[0]))
         e1['values']=lt
         db.close() 
    def checkdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur=db.cursor()
         xa=e1.get()
         sql="select count(*) from callfeedback where callid='%s'"%(xa)
         cur.execute(sql)
         data=cur.fetchone()
         if data[0]==0:
             messagebox.showinfo('hi','ID Available')
         else:
             messagebox.showinfo('not  available','ID already Exist')
             db.close()
    def savedata():
        db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
        cur = db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        if not xa or not xb or not xc:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        sql="insert into callfeedback values('%s','%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','your data is save')
        sendemailcustomer()
        delete()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    def delete():
         db = pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur = db.cursor()
         xa=e1.get()
         
         if not xa  :
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
         sql="delete from callregister where callid='%s'"%(xa)
         cur.execute(sql)
         db.commit()
         db.close()
         messagebox.showinfo('Hi','Successfukky Deleted from callregister')
         e1.delete(0,100)
 
    def sendemailcustomer():
        from_address = "luckymishra741756@gmail.com"
        to_address = e4.get()
    
        rating_value = e2.get()
        remarks_value = e3.get()
    
        msg = MIMEMultipart('alternative')
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Thank You for Your Feedback"
    
        if "5" in rating_value:
            tone = (
                "We're thrilled to hear that you had a great experience with us. "
                "Your kind words and 5-star rating truly motivate our team to continue delivering top-notch service."
            )
        elif "4" in rating_value:
            tone = (
                "We're happy to know that you’re satisfied with our service. "
                "Thank you for your positive feedback! We'll keep working to earn that 5th star."
            )
        elif "3" in rating_value:
            tone = (
                "Thank you for your feedback. We understand there's room for improvement "
                "and we’re committed to making your next experience even better."
            )
        elif "2" in rating_value:
            tone = (
                "We appreciate you sharing your experience, though we're sorry to hear that it didn’t meet your expectations. "
                "Your input is important and will be used to improve our service."
            )
        elif "1" in rating_value:
            tone = (
                "We sincerely apologize for the inconvenience you faced. "
                "Your feedback is crucial, and our team will review it carefully to take corrective action."
            )
        else:
            tone = (
                "Thank you for your time. Your feedback helps us understand customer needs better."
            )
    
        body = (
            f"Dear Customer,\n\n"
            f"{tone}\n\n"
            f"Here is a summary of the feedback you provided:\n"
            f"• Rating: {rating_value}\n"
            f"• Remarks: {remarks_value}\n\n"
            "If you wish to share more, feel free to reply directly to this email:luckymishra741756@gmail.com\n\n"
            "Thank you once again for trusting our service center.\n\n"
            "Warm regards,\n"
            "Customer Relations Team\n"
            "Service Center"
        )
    
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
        username = 'luckymishra741756@gmail.com'
        password = 'nttxdlfyrcprgyce'
    
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            messagebox.showinfo('Success', 'Feedback email sent to customer successfully.')
        except Exception as e:
            messagebox.showerror('Email Error', f'Failed to send email:\n{str(e)}')

    z=Label(t,text='Insert into Call Feedback',font=("Segoe UI", 24, "bold"), fg="#0A3D62", bg="white", relief="raised")
    z.place(x=180,y=50)    
        
    a=Label(t,text='Call ID :',font=('arial',15))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,width=20,font=('arial',17))
    filldata()
    e1.place(x=350,y=150)
         
    
    b=Label(t,text='Feedback Rating:',font=('arial',15))
    b.place(x=100,y=200)
    values = [ '1 star ', '2 stars', '3 stars', 
    '4 stars', '5 stars',"Not interested in Rating"]
    e2=Spinbox(t,values=values,font=('arial',15),width=23)
    e2.place(x=350,y=200)
  
    
    c=Label(t,text='Remarks :',font=('arial',15))
    c.place(x=100,y=250)
    e3=Entry(t,width=25,font=('arial',15))
    
    e3.place(x=350,y=250)

      
    f=Label(t,text='Email(Customer):',font=('arial',15))
    f.place(x=100,y=300)
    e4=Entry(t,width=25,font=('arial',15))
    e4.place(x=350,y=300)
    
    
        
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
    
    
        
    btn3=Button(t,text='Check',bg="#0f4c75", fg="white",width=6,
                    font=("Segoe UI", 9, "bold"), relief="raised", padx=10, pady=5,
                    cursor="hand2",command=checkdata)
    btn3.place(x=635,y=148)
    
    t.mainloop()