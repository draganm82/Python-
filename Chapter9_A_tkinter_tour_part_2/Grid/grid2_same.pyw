"""
build pack and grid forms on different frames in same window;
can't grid and pack in same parent container (e.g., root window)
but can mix in same window if done in different parent frames;
"""
from tkinter import*
from grid2 import gridBox, packBox

root =Tk()

Label(root, text='Grid:').pack()
frm = Frame(root, bd=5, relief = RAISED)
frm.pack(padx=5, pady=5)
gridBox(frm) 

Label(root, text='Pack:').pack()
frm = Frame(root, bd=5, relief=RAISED)
frm.pack(padx=5, pady=5)
packBox(frm)

Button(root, text='Quit', command=root.quit).pack()
mainloop()