from tkinter import *
from grid2 import gridBox, packBox
root = Tk()
gridBox(root)
packBox(root)
Button(root, text='Quit', command=root.quit).pack()
mainloop()