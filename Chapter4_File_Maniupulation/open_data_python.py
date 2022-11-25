"""
file = open('data.txt')     # open input file object: 'r' default
lines = file.readlines()  # read into line string list
for line in lines:          # BUT use file line iterator! (ahead)
    print(line, end='')
""" #this type of algorithm is used in older versiion of python
"""
for line in open ('data.txt'): # even shorter: temporary file object
    print (line, end ='')"""    # auto-closed when garbage collected

"""
working version of the  python 3.1 or above """

file = open ('data.txt')
for line in file:   # no need to call readlines
    print(line, end='') # iterator reads next line each time

"""file = open ('data.txt') # iterators: exception at EOF
file.__next__() # no need to call iter(file) first,
'Hello file world!\n'  # since files are their own iterator
file.__next__()
'Bye file world."""

"""file = open('data.txt')     # open input file object: 'r' default
lines = file.read(),     # read into line string list
for line in lines:          # BUT use file line iterator! (ahead)
    print(line, end='') """
