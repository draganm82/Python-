from tkinter import Label                               # get a widget object
widget = Label(None, text='Hello GUI world')            # make one
widget.pack()                                           # arrange itw
widget.mainloop()                                       # start event loop
def mainloop():
while the main window has not been closed:
if an event has occurred:
run the associated event handler function