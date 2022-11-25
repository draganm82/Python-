import os
pipe = os.popen ('hello_out.py')
print(pipe.read())
print (pipe.close())