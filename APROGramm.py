from tkinter import * 
aken=Tk() #создаем окно
aken.title("FOTOROBOT")
aken.geometry("700x1000")
f1=Frame(aken,width=200,height=500)
f1.pack(side=LEFT)
f2=Frame(aken,width=500,height=500)
f2.pack(side=RIGHT)
c_=Canvas(f2, width=500, height=500, bg="Lightblue")
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
c=0

def nägu():
    pass
def silm1():
    pass
def silm2():
    pass
def nina():
    pass
def suu():
    pass
c1=Checkbutton(f1,text="nägu",variable=CheckVar1, font="Calibri 26", command=...)
c1.pack()
c2=Checkbutton(f1,text="silm1",variable=CheckVar2, font="Calibri 26", command=...)
c2.pack()
c3=Checkbutton(f1,text="silm2",variable=CheckVar3, font="Calibri 26", command=...)
c3.pack()
c4=Checkbutton(f1,text="nina",variable=CheckVar4, font="Calibri 26", command=...)
c4.pack()
c5=Checkbutton(f1,text="suu",variable=CheckVar5, font="Calibri 26", command=...)
c5.pack()

c_.pack()
aken.mainloop()