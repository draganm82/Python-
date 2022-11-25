from tkinter import *
from multiprocessing import Process
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']
def runDemo(modname): # run in a new process
    module = __import__(modname) # build gui from scratch
    module.Demo().mainloop()
    if __name__ == '__main__':
        for modname in demoModules: # in __main__ only!
            Process(target=runDemo, args=(modname,)).start()

    root = Tk() # parent process GUI
    root.title('Processes')
    Label(root, text='Multiple program demo: multiprocessing', bg='white').pack()
    root.mainloop()