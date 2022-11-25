""""
open ('file').read #read entire file into string
open ('file').read(N) #read next N bytes into string 
open ('file').readlines() #read entire file into line string list
open ('file').readline #read next line throught '\n'
"""


file = open ('spam.txt', 'w') #create file spam
file.write(('spam' *5) +'\n') #write text return character written 

file.close()

file=open('spam.txt') #or open file (spam.txt)
text = file.read() 
print(text)