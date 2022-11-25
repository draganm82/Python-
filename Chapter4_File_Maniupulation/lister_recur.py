import sys, os

def mylister(currdir):
    print('[' +currdir+ ']')
    for file in os.listdir(currdir):    # list files hbere
        path = os.path.join(currdir, file) # add dir path BACK
        if not os.path.isdir(path):
            print (path)
        else:
            mylister(path)  # recur into subdirs
            if __name__=='__main__': 
                mylister(sys.argv[1])