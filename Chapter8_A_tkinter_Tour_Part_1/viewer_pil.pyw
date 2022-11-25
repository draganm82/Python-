"""
show one image with PIL photo replacement object
handles many more image types; install PIL first: placed in Lib\site-packages
"""

import os, sys
from tkinter import*
from PIL.ImageTk import PhotoImage   # <== use PIL replacement class

imgdir='E:\Jana slike more'
imgfile='_MG_8214.JPG'

if len (sys.argv)>1:
    imgfile =sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())  # show size in pixels on exit