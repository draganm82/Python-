file = open('random.bin','r' ) # text mode ok if no encoding/endlines
reclen =8
file.seek(reclen*3)            # fetch record 4

file.read(reclen)

file.seek(reclen*1)            # fetch record 2

file.read(reclen)
file = open('random.bin', 'rb') # binary mode works the same here
file.seek(reclen * 2) # fetch record 3
file.read(reclen) # returns byte strings