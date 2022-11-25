import sys
from tkinter import *

widget = Label(None, text='opa pa i ne radi bas')
widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack(expand = NO, fill=X)
widget.mainloop()