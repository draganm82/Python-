import sys

#read number till eof and show squares

def interact():
    print ('Hello stream world')   # print sends to sys.stdout
    while True:
        try:
            reply = input('Enter a number>')        #input reads sys.stdin
        except EOFError:    #raise an except on eof
                 break          # input given as a string
        else:
                num = int (reply)
                print ("%d squared is %d" % (num, num ** 2))
    print ('Bye')
if __name__ == '__main__':
    interact()
