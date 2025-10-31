import pymysql
from tkinter import *
from tkinter import messagebox

def show_security_verification():
    root = Tk()
    root.geometry("750x600")
    root.title("Security Questions Verification")
    root.configure(bg="#f0f2f5")

    Label(root, text="Username:", font=("Segoe UI", 14), bg="#f0f2f5").place(x=80, y=40)
    entry_username = Entry(root, font=("Segoe UI", 14), width=25)
    entry_username.place(x=200, y=40)

    # Fixed Questions Labels
    q1_label = Label(root, text="Q1: What is your pet's name?", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q1_label.place(x=80, y=100)
    Label(root, text="Ans 1:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=125)
    a1_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a1_entry.place(x=150, y=125)

    q2_label = Label(root, text="Q2: What is your birthplace?", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q2_label.place(x=80, y=180)
    Label(root, text="Ans 2:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=205)
    a2_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a2_entry.place(x=150, y=205)

    q3_label = Label(root, text="Q3: What is your favorite food?", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q3_label.place(x=80, y=260)
    Label(root, text="Ans 3:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=285)
    a3_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a3_entry.place(x=150, y=285)

    q4_label = Label(root, text="Q4: What is your favorite color?", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q4_label.place(x=80, y=340)
    Label(root, text="Ans 4:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=365)
    a4_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a4_entry.place(x=150, y=365)

    q5_label = Label(root, text="Q5: What is yoursruname ?", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q5_label.place(x=80, y=420)
    Label(root, text="Ans 5:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=445)
    a5_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a5_entry.place(x=150, y=445)

    def savedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
    
        x = entry_username.get()
        x1 = q1_label.cget("text")[4:]
        x2 = a1_entry.get()
        x3 = q2_label.cget("text")[4:]
        x4 = a2_entry.get()
        x5 = q3_label.cget("text")[4:]
        x6 = a3_entry.get()
        x7 = q4_label.cget("text")[4:]
        x8 = a4_entry.get()
        x9 = q5_label.cget("text")[4:]
        x10 = a5_entry.get()
    
        if not x or not x2 or not x4 or not x6 or not x8 or not x10:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return False
    
        # Use parameterized query to avoid apostrophe/syntax issues
        sql = "INSERT INTO securityinfo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
    
        db.commit()
        messagebox.showinfo('Saved', 'Your data is saved successfully.')
        root.destroy()

    def checkdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='servicecenter')
         cur=db.cursor()
         x = entry_username.get()
         sql="select count(*) from securityinfo where username='%s'"%(x)
         cur.execute(sql)
         data=cur.fetchone()
         if data[0]==0:
             messagebox.showinfo('hi','ID Available')
         else:
             messagebox.showinfo('not  available','ID already Exist')
             db.close()
   

    btn_verify = Button(root, text="Save Answers", font=("Segoe UI", 14), bg="#27ae60", fg="white", command=savedata)
    btn_verify.place(x=300, y=510)
    
    btn_load = Button(root, text="check", font=("Segoe UI", 12), bg="#2980b9", fg="white", command=checkdata)
    btn_load.place(x=530, y=35)
    
    root.mainloop()

show_security_verification()
