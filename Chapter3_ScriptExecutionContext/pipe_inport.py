import os
pipe = os.popen ('hello_in.py', 'w')    #'w' --write to program stdin
pipe.write('Gumby\n')

pipe.close()                            # \n at end is optional
open ('hello-in.txt').read()            # output sent to a file