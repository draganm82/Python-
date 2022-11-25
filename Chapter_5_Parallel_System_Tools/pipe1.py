import os, time
def childs(pipeout):
    zzz=0
    while True:
        time.sleep(zzz)         # make parent wait
        msg = ('Spam %03d' %zzz).encode()   # pipes are binary bytes
        os.write(pipeout, msg)      # send to parent
        zzz= (zzz+1) %5         # goto 0 after 4
def parent ():                  # make 2-ended pipe
    pipein, pipeout = os.pipe()
    if os.getpid() == 0:
        child(pipeout)
    else:
        while True:
            line = os.read(pipein,32)
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

parent()