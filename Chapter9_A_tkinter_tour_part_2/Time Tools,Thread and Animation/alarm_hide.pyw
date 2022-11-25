# customize to erase or show button on after() timer callbacks

from tkinter import*
import alarm

class Alarm(alarm.Alarm):   # change alarm callback
    def __inint__(self,msecs=1000): # default = 1 second
        self.shown = False
        alarm.Alarm.__inint__(self, msecs)

    def repeater(self): # on every N millisecs
        self.bell()  # beep now
        if self.shown:          # hide or erase button now
            self.stopper.pack_forget()  # or reverse colors, flash...
        else:
            self.stopper.pack()
            self.shown = not self.shown # toggle state for next time
            self.after(self.msecs, self.repeater)  # reschedule handler
            
if __name__ == '__main__': Alarm(msecs=500).mainloop()