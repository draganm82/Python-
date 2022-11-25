import sys
from tkinter import*
makemodel = (len(sys.argv)>1)

def dialog():
    win= Toplevel()                                     # make a new window
    Label(win, text='Hard drive reformatted!').pack()   # add a few widgets
    Button(win, text='OK', command=win.destroy).pack()  # set destroy callback
    if makemodel:
        win.focus_set()         # take over input focus,
        win.grab_set()          # disable other windows while I'm open,
        win.wait_window()       # and wait here until win destroyed
        win.wait_visibility(22)
    print('dialog exit')        # else returns right away
root = Tk()
Button (root, text='popup', command=dialog).pack()
root.mainloop()