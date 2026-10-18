import subprocess
subprocess.call("cls",shell=True)
data="=================\n"
sabad=0
s1=1 ;s2=0 ; s3=0
while True:
    food=input("enter food name")
    if food=="":
        break
    tedad=float(input("tedad:"))
    price=float(input("price:"))
    tax=float(input("tax:"))

