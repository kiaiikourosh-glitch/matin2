import subprocess
subprocess.call("cls",shell=True)
from tkinter import messagebox 
from tkinter import ttk
from tkinter import *
show="off"
from random import*
user=0; machine=0 

def createcode():
    code=randint(1,3)
    if code==1:
        return "kagfhaz"
    if code==2:
        return "Sang"  

    if  code==3:
        return "gheichi"



def game_page():
    def run():
        gameuser=e1.get()
        if gameuser not in ["sang","kaghaz","gheichi"]:
            e1.focus()
            return

        gamemachine=createcode()
        global user ,machine
        if gameuser=="sang" and gamemachine=="gheichi" or gameuser=="ghichi" and gamemachine=="kaghaz" or  gameuser=="sang"
        user+=1
        if gameuser=="gheichi" and gamemachine=="sang" or gameuser=="kaghaz"and gamemachine=="gheichi"  or gameuser=="sang"
        machine+=1
        data="user="+str(user)+ machine  ,+str(machine)
        e3.delete(0,END)
        e3.insert(0,data)
        if user==3 or machine==3:
            b1.config(satate="disabbled")
    p1=Tk()
    p1.title("Game")
    p1.geometry("500x300")

    l1=Label(p1,text="game")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)


    l2=Label(p1,text="machine")
    l2.place(x=10,y=60)
    e2=Entry(p1)
    e2.place(x=100,y=60)


    l3=Label(p1,text="resault")
    l3.place(x=10,y=110)
    e3=Entry(p1)
    e3.place(x=100,y=110)

    b1=Button(p1,text="run",command=run)
    b1.place(x=300,y=10)
    p1.mainloop()
first_page()








        