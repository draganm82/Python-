import sys

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':           # find "-name value" pairs
            opts[argv[0]] = argv[1]    # dict key is "-name" arg
            argv=argv[2:]
        else:
            argv  = argv[1:]
    return opts

if __name__=='__main__':
    from sys import argv        #example client code 
    myargs = getopts (argv)
    if '-i' in myargs:
        print (myargs['-i'])
    print(myargs)
