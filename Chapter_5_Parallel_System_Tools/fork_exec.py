"starts programs until you type 'q'"

import os

parm =0
while True:
    parm +=1
    pid = os.getpid()
    if pid ==0:             # copy process
        os.execlp('python', 'python', 'child.py', str(parm))  # overlay program
        assert False, 'error string program ' # shouldn't return
    else:
        print('Child is', pid)
        if input() == 'q':break