import sys
from tkinter import *

def quit():         # a custom callback handler
    print('Hello, I must be going...') #kill windows and process
    sys.exit()

root=Tk()

Button(None, text='Hello event world', command = quit, command=bell())
root.pack( side=LEFT)
root.mainloop()