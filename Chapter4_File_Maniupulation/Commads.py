from sys import argv
from File_Scanners import scanner

class UnknownCommand (Exception): pass

def processLine(line):          # define a function
    if line[0] == '*':           # applied to each line
        print("Ms.",line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])  # strip first and last char: \n
    else:
        raise UnknownCommand(line)  # raise an exception

filename = 'data.txt'
if len(argv) == 2: filename = argv[1] # allow filename cmd arg
scanner(filename, processLine) # start the scanner