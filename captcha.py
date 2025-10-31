# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:57:24 2025

@author: user
"""

from tkinter import ttk
import tkinter
from tkinter import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
import random
t=tkinter.Tk()
t.geometry('800x800')
captext=''
def gen():
    image=ImageCaptcha(width=100,height=100)
    r=random.random()*35000
    st=str(round(r))
    x=random.random()*90
    st1=chr(round(x))
    global captext
    captext=st1 + st
    data=image.generate(captext)
    image.write(captext,'captchaone.png')
    messagebox.showinfo('Hi','Captcha Generated')

def show():
    img=PhotoImage(file='Captchaone.png')
    a.config(image=img)
    a.image=img
    global captext
    print(captext)

def login():
    if e1.get()=='ashish' and e2.get()=='0116' and e3.get()==captext:
        messagebox.showinfo('Hi','Login Successfully')
    else:
        messagebox.showinfo('Hi','Login Failed')

btn=Button(t,text='Generate Captcha',command=gen)
btn.place(x=300,y=50)

btn1=Button(t,text='Show Captcha',command=show)
btn1.place(x=300,y=100)



a=Label(t,text='My Captcha')
a.place(x=300,y=500)

b=Label(t,text='Login')
b.place(x=50,y=200)

e1=Entry(t,width=20)
e1.place(x=150,y=200)


c=Label(t,text='Password')
c.place(x=50,y=250)

e2=Entry(t,width=20)
e2.place(x=150,y=250)


d=Label(t,text='Captcha')
d.place(x=50,y=300)

e3=Entry(t,width=20)
e3.place(x=150,y=300)

btn2=Button(t,text='login',command=login)
btn2.place(x=200,y=350)





t.mainloop()