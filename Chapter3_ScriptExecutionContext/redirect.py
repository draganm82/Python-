import sys

class Output: #simulated output file
    def __init__(self):
        self.text =' '  #empty string when created
    def write(self, string): #add string of bytes
        self.text +=string
    def writelines(self, lines):
        for line in  lines: self.write(line)

#class output text is finished

class Input:                #simulated input file
    def __init__(self, input = ' ') #default argument
        self.text = input             #save string when created
    def read(self, size=None):      #otional argument 
        if size == None:               #read N bytes or all
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
            return res

    def readlie(self):
        eoln=self.text.find('\n') #find offset of next eoln
        if eoln == -1:              #slixe off through eoln
            res, self.text = self.text, '' 
        else:
            res, self.text = self.text[:eoln +1], self.text[eoln +1:]
            return res
            #class read line is finished

    def redirect (function, pargs, kargs, input):   #redirect stdin/out
        savestreams = sys.stdin, sys.stdout     #run a function object
        sys.stdin = Input(input)        #return stdout text
        sys.stdout = Output()

        try:
            result = function (*pargs, **kargs) #run function with args
            output = sys.stdout.text 
        finally:
            sys.stdin, sys.stdout = savestream #restore if exc or not
            return (result, output) #return result if no exc
