# Tk8.0 style top-level window menus
from tkinter import*                    # get widget classes
from tkinter.messagebox import*         # get standard dialogs
import os,sys
def notdone():
    showerror('Not implemented', 'Not yet available')

def makemenu(win):
    top= Menu(win)                        # win=tsop-level window
    win.config(menu=top)                  # set its menu option
    
    file = Menu(top)
    file.add_command(label='New....', command= notdone, underline=0) #can be import the definition (function) from other GUI chapters and tools such is command for new
    file.add_command(label='Open...', command=notdone, underline=0) #command for open, 
    file.add_command(label='Quit',  command=win.quit,  underline=0) #implemented command quit
    top.add_cascade(label='File', menu=file,         underline=0)

    edit = Menu(top, tearoff = False)
    edit.add_command(label='Cut',     command=notdone, underline=0)
    edit.add_command(label='Paste',   command =notdone, underline=0)
    edit.add_separator()
    top.add_cascade(label  = 'Edit',  menu=edit,        underline=0)
    
    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam',  command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command = notdone, underline=0)
    edit.add_cascade(label = 'Stuff', menu=submenu,       underline=0)

if __name__=='__main__':
    root=Tk()                   # or Toplevel()
    root.title('menu_win')       # set window-mgr info
    makemenu(root)               # associate a menu bar
    msg = Label(root, text='Windows menu basic')
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()   