import struct

file= open ('data.bin', 'wb')
bytes = file.read()
values = struct.unpack('i4shf')
print (values)