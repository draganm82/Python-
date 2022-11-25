# simple 2D table, in default Tk root window
from tkinter import*
for i in range (39):
    for j in range(3):
        lab=Label(text='%d.%d'%(i,j),relie=RIDGE)
        lab.grid(row=i, column=j,sticky=NSEW)
mainloop()
