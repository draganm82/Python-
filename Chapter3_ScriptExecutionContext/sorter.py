import sys 
lines = sys.stdin.readlines() #sort stdin lines 
lines.sort()                  #send result to stdout
for line in lines: print (line, end='') #for  futher processing 
    