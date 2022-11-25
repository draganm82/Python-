jpgdir="E:\\Jana slike more"

from tkinter import*
win=Tk()
igm=PhotoImage(file= jpgdir +"_MG_8214.JPG")
can=Canvas(win)
can.pack(fill=BOTH)
can.create_image(2,2,image=igm, anchor = NW)
win.mainloop()