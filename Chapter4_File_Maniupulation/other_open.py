file = open('data.txt' ,'a' )   # open in append mode: doesn't erase
file.write('the livfe of Mounty Python')
file.close()

print (open ('data.txt').read())