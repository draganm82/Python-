import os, sys, find # here, gets Tools.find

count = 0
try: 
    for filename in find.find('*.pyc', sys.argv[1]):
        count += 1
        print(filename)
        os.remove(filename)
except:
   print ("ovo sam ja")

print('Removed %d .pyc files' % count)