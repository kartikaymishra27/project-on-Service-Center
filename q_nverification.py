import pymysql
from tkinter import *
from tkinter import messagebox
from maindashboardpassword import *
def show_security_verification():
    root = Tk()
    root.geometry("750x600")
    root.title("Security Questions Verification")
    root.configure(bg="#f0f2f5")

    Label(root, text="Username:", font=("Segoe UI", 14), bg="#f0f2f5").place(x=80, y=40)
    entry_username = Entry(root, font=("Segoe UI", 14), width=25)
    entry_username.place(x=200, y=40)

    q1_label = Label(root, text="Q1:", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q1_label.place(x=80, y=100)
    Label(root, text="Ans 1:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=125)
    a1_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a1_entry.place(x=150, y=125)

    q2_label = Label(root, text="Q2:", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q2_label.place(x=80, y=180)
    Label(root, text="Ans 2:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=205)
    a2_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a2_entry.place(x=150, y=205)

    q3_label = Label(root, text="Q3:", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q3_label.place(x=80, y=260)
    Label(root, text="Ans 3:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=285)
    a3_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a3_entry.place(x=150, y=285)

    q4_label = Label(root, text="Q4:", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q4_label.place(x=80, y=340)
    Label(root, text="Ans 4:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=365)
    a4_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a4_entry.place(x=150, y=365)

    q5_label = Label(root, text="Q5:", font=("Segoe UI", 12), bg="#f0f2f5", wraplength=550, justify=LEFT)
    q5_label.place(x=80, y=420)
    Label(root, text="Ans 5:", font=("Segoe UI", 12), bg="#f0f2f5").place(x=80, y=445)
    a5_entry = Entry(root, font=("Segoe UI", 12), width=15)
    a5_entry.place(x=150, y=445)

    stored_answers = []

    def load_questions():
        uname = entry_username.get().strip()
        if not uname:
            messagebox.showwarning("Input Error", "Please enter your username first.")
            return

        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
            cur = db.cursor()
            cur.execute("SELECT q1, q2, q3, q4, q5, a1, a2, a3, a4, a5 FROM securityinfo WHERE username = %s", (uname,))
            result = cur.fetchone()
            db.close()

            if not result:
                messagebox.showerror("Not Found", "No security info found for this username.")
                return

            q1_label.config(text=f"Q1: {result[0]}")
            q2_label.config(text=f"Q2: {result[1]}")
            q3_label.config(text=f"Q3: {result[2]}")
            q4_label.config(text=f"Q4: {result[3]}")
            q5_label.config(text=f"Q5: {result[4]}")

            a1_entry.delete(0, END)
            a2_entry.delete(0, END)
            a3_entry.delete(0, END)
            a4_entry.delete(0, END)
            a5_entry.delete(0, END)

            nonlocal stored_answers
            stored_answers = result[5:]  # a1 to a5

        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    
    def emailget():
        login_id=entry_username.get().strip()
        db = pymysql.connect(host='localhost', user='root', password='root', database='servicecenter')
        cur = db.cursor()
        cur.execute("SELECT email FROM logindata WHERE loginid = %s", (login_id,))
        result = cur.fetchone()
         
        if result:
            email = result[0]
            messagebox.showinfo(
                'Registered Email',
                f'Dear {login_id},\n\nYour registered email address is:\n{email}\n\nPlease ensure this email is kept up-to-date.'
            )
        else:
            messagebox.showerror(
                'User Not Found',
                f'No account found for Login ID: {login_id}'
            )

    def verify_answers():
        if not stored_answers:
            messagebox.showwarning("Load Required", "Please load questions first.")
            return

        input_answers = [
            a1_entry.get().strip().lower(),
            a2_entry.get().strip().lower(),
            a3_entry.get().strip().lower(),
            a4_entry.get().strip().lower(),
            a5_entry.get().strip().lower()
        ]
        correct_answers = [ans.strip().lower() for ans in stored_answers]

        if input_answers == correct_answers:
            messagebox.showinfo("Success", "All answers matched successfully!")
            showpass()
            root.destroy()
        else:
            messagebox.showerror("Verification Failed", "One or more answers are incorrect.")

    btn_load = Button(root, text="Load Questions", font=("Segoe UI", 12), bg="#2980b9", fg="white", command=load_questions)
    btn_load.place(x=530, y=35)

    btn_verify = Button(root, text="Verify Answers", font=("Segoe UI", 14), bg="#27ae60", fg="white", command=verify_answers)
    btn_verify.place(x=300, y=510)

    root.mainloop()