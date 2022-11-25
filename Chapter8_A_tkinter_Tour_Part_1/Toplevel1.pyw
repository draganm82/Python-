import tkinter
from  tkinter import Tk, Button
tkinter.NoDefaultRoot()

win1= Tk()   # on default Tk() root window
win2 =Tk()

Button(win1,text='Spam', command=win1.destroy).pack()
Button(win1,text='Spam', command=win2.destroy).pack()

win1.mainloop()

