from tkinter import * 
aken=Tk() #создаем окно
aken.title("FOTOROBOT")
aken.geometry("700x1000")
f1=Frame(aken,width=200,height=500)
f1.pack(side=LEFT)
f2=Frame(aken,width=500,height=500)
f2.pack(side=RIGHT)
c_=Canvas(f2, width=500, height=500, bg="Lightblue")
CheckVar1 = StringVar()
CheckVar2 = StringVar()
CheckVar3 = StringVar()
CheckVar4 = StringVar()
CheckVar5 = StringVar()

a=""
b=""
c=""
d=""
e=""
f=""
g=""


def nägu():
    global a
    if CheckVar1.get()=="nägu":
        a=c_.create_oval((5, 5, 480, 480), outline="grey", fill="pink")
    else:
        c_.delete(a)
def silm1():
    global b,c
    if CheckVar2.get()=="silm1":
        b=c_.create_oval((72,72,130,130)) # 1- y-верхняя точка глаза, 2- x-левая точка глаза, 3- y-нижней точки глаза, 4- x-правая точка глаза
        c=c_.create_oval((82,82,117,120),fill="black")
    else:
        c_.delete(b)
        c_.delete(c)
def silm2():
    global d,e
    if CheckVar3.get()=="silm2":
        d=c_.create_oval((165,72,221,130))
        e=c_.create_oval((175,82,211,120),fill="black")
    else:
        c_.delete(d)
        c_.delete(e)
def nina():
    global f
    if CheckVar4.get()=="nina":
        f=c_.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")
    else:
        c_.delete(f)
def suu():
    global g
    if CheckVar5.get()=="suu":
        g=c_.create_line((213, 215, 90, 215),fill="black",width=2)
    else:
        c_.delete(g)

c1=Checkbutton(f1,text="nägu",variable=CheckVar1, onvalue="nägu", offvalue="tühi", font="Calibri 26", command=nägu) 
c1.pack()
c1.deselect()
c2=Checkbutton(f1,text="silm1",variable=CheckVar2, font="Calibri 26", onvalue="silm1", offvalue="tühi", command=silm1)
c2.pack()
c2.deselect()
c3=Checkbutton(f1,text="silm2",variable=CheckVar3, font="Calibri 26", onvalue="silm2", offvalue="tühi", command=silm2)
c3.pack()
c3.deselect()
c4=Checkbutton(f1,text="nina",variable=CheckVar4, font="Calibri 26", onvalue="nina", offvalue="tühi", command=nina)
c4.pack()
c4.deselect()
c5=Checkbutton(f1,text="suu",variable=CheckVar5, font="Calibri 26", onvalue="suu", offvalue="tühi", command=suu)
c5.pack()
c5.deselect()

c_.pack()
aken.mainloop()