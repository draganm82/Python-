from tkinter import*
colors = ['red', 'green', 'orange','white', 'yellow', 'blue']

r=0
for c in colors:
    Label(text=c, relief=RIDGE, width=25).grid(row=r, column =1)
    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r, column=2)
    r += 1
mainloop()
