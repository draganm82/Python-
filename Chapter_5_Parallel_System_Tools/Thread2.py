import _thread  # all 3 print 4294967296

def action(i):          # function run in threads
    print(i**32)

class Power:
    def __init__(self, i):
        self.i=i
    def action (self):          # bound method run in threads
        print(self.i **32)

_thread.start_new_thread(action,(2)) # bound method run in threads

_thread.start_new_thread((lambda: action (2)), ())  # lambda function to defer

obj  = Power(2)

_thread.start_new_thread(obj.action, ()) # bound method object