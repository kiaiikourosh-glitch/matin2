import subprocess
subprocess.call("cls",shell=True)
from tkinter import messagebox 
from tkinter import ttk
from tkinter import *



def login_matimn():  
    def mohasebeh():
        vaznard=float(e1.get())
        gheimatard=float(e7.get())

        vaznshekar=float(e2.get())                    
        gheimatshekar=float(e8.get())

        vaznkhameh=float(e3.get())
        gheimatkhameh=float(e9.get())


        vaznmiveh=float(e4.get())
        gheimatmiveh=float(e10.get())

        hazinehard=vaznard*gheimatard
        hazinehshekar=vaznshekar*gheimatshekar
        hazinehkhameh=vaznkhameh*gheimatkhameh
        hazinehmiveh=vaznmiveh*gheimatmiveh

        gheimatkol=hazinehard+hazinehkhameh+hazinehmiveh+hazinehshekar
        sod=float(e5.get())
        forosh=gheimatkol+gheimatkol*sod /100
        e10.delete(0,END)
        e10.insert(0,forosh)



    p1=Tk()
    p1.geometry("900x600")
    p1.title("bakery")
    p1.config(bg="#9C3131")

    l1=Label(p1,text="ard")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)


    l2=Label(p1,text="shekar")
    l2.place(x=10,y=50)
    e2=Entry(p1)
    e2.place(x=100,y=50)


    l3=Label(p1,text="khameh")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)


    l4=Label(p1,text="miveh")
    l4.place(x=10,y=130)
    e4=Entry(p1)
    e4.place(x=100,y=130)


    l5=Label(p1,text="sod %")
    l5.place(x=10,y=170)
    e5=Entry(p1)
    e5.place(x=100,y=170)

    l6=Label(p1,text="last price")
    l6.place(x=10,y=210)
    e6=Entry(p1)
    e6.place(x=100,y=210)


    e7= Entry(p1)
    e7.place(x=300,y=10)
    
    e8= Entry(p1)
    e8.place(x=300,y=50)

    e9= Entry(p1)
    e9.place(x=300,y=90)


    e10= Entry(p1)
    e10.place(x=300,y=130)

    b1=Button(p1,text="calculate",command=mohasebeh)
    b1.place(x=500,y=10)






    p1.mainloop()
login_matimn()