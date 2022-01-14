from tkinter import*

def dis_coor(event):
    myl["text"]=f"x={event.x} y={event.y}"
myw=Tk()
myc=Canvas(myw,width=500,height=500)
myl=Label(bd=4,relief="solid",font="Times 22 bold",bg="white",fg="black")
myc.bind("<Button-1>",dis_coor)
myc.grid(row=0,column=0)
myl.grid(row=1,column=0)

#
myc.create_oval((5, 5, 480, 480))
myc.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")
myc.create_line((213, 215, 90, 215),fill="black",width=2)

myc.create_oval((133,92,177,130)) # 1- y-верхняя точка глаза, 2- x-левая точка глаза, 3- y-нижней точки глаза, 4- x-правая точка глаза
myc.create_oval((165,72,221,130))

myc.create_oval((82,82,117,120),fill="black")
myc.create_oval((175,82,211,120),fill="black")

myw.mainloop()