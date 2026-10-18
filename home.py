import subprocess
subprocess.call("cls",shell=True)
from tkinter import messagebox 
from tkinter import ttk
from tkinter import *
show="off"
from random import *
def create_captcha():
    cap=randint(1000,9999)
    return cap


    def sign_in():
        user=e1.get()
        if user!="matin":
            e1.focus()
            return
        password=e2.get()
        if password!="123456":
            e2.focus()
            return
        mycap=e3.get()
        syscap=e4.get()
        if mycap!=syscap:
            e3.focus()
            return        

    
        p1.destroy()
        maharatsara()

    def showpassword():
        global show
        if show=="off":
            show="on"
            e2.config(show="")
            b2.config(text="😁")

        else:
            show="off"
            e2.config(show="•")
            b2.config(text="😒")
    def new_captcha():
        cap=create_captcha()
        e4.delete(0,END)
        e4.insert(0,cap)
        
    p1=Tk()
    p1.title("login_page")
    p1.geometry("600x400")
    p1.resizable(False,False)
    p1.config(bg="#34414E")

    l1=Label(p1,text="user  :")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)
    

    l2=Label(p1,text="password:")
    l2.place(x=10,y=50)
    e2=Entry(p1,show="•")
    e2.place(x=100,y=50)
    b2=Button(p1,text="😯",command=showpassword)
    b2.place(x=240,y=50)


    l3=Label(p1,text="security code:")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

  
    l4=Label(p1,text="code:")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)
    cap=create_captcha()
    e4.insert(0,cap)

    
    b4=Button(p1,text="new",command=new_captcha)
    b4.place(x=240,y=130)

    b1=Button(p1,width=17,text="Sign_In",command=sign_in)
    b1.place(x=100,y=170)


    p1.mainloop()


def maharatsara():

    def  log_out():
        q=messagebox.askyesno("log_out","do you want leave ?")

        if q==True:
            p1.destroy()
            login_page()
    p1=Tk()
    p1.title("logout")
    p1.geometry("900x400")
    p1.resizable(False,False)
    p1.config(bg="#CDF23A")

    l1=Label(p1,text="Kala:")
    l1.place(x=10,y=50)
    e1=Entry(p1)
    e1.place(x=100,y=50)

    l2=Label(p1,text="price:")
    l2.place(x=10,y=50)
    e2=Entry(p1)
    e2.place(x=100,y=50)

    l3=Label(p1,text="TEDAD :")
    l3.place(x=10,y=10)
    e3=Entry(p1)
    e3.place(x=100,y=10)

    l4=Label(p1,text="tax:")
    l4.place(x=10,y=50)
    e4=entry=(p1)
    e4.place(x=100,y=10)

    b1=Button(p1,text="sign_out",command=log_out)
    b1.place(x=150,y=150)


   
    p1.mainloop()
login_page()