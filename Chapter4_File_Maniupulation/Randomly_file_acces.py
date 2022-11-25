""" records = [bytes([char]*8) for char in b'spam']
print(records)

file = open('random.bin', 'w+b' )
for rec in records:         #write four records
    size = file.write (rec) #bytes for binary mode

file.flush()
pos = file.seek(0)      #read entire file
print (file.read())

file = open ('random.bin', 'r+b')
print (file.read()) """

record = b*'X' *8
file.seek(0)        # update first record
file.write(record)
file.seek(len(record) *2) # update third record
file.write (b 'Y' *8)

file.seek(8)
file.read(len(record))

file seek(0)
file.read()
