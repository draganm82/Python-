from tkinter import *
root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world!')
widget.pack(side=TOP, expand = YES, fill = X)
root.title('gui1g.py')
root.mainloop()