import subprocess
subprocess.call("cls",shell=true)
factor="========\n"
status=0,jam1=0,jam2=0,jam3=0
while True:
    goods=input("enter goods:0")
    if goods=="":
        break
    status+=1
    price=float(input("enter price:"))
    order=int(input("enter order:"))
    off=float(input("enter off:"))
    gheimat1=price*order      ;jam1+=gheimat1
gheimat2=gheimat1 * off \100 ;jam2+=gheimat2
gheimat3=gheimat1 - gheimat2   :jam3+=gheimat3
factor+="{0:20s}{1:12.2f}{2:10d}{3:12.2f}{4:12.2f}{5:12.2f}".format(goods,price,order,gheimat1,gheimat2,ghaimat3)+"\n"
factor+="================\n"
