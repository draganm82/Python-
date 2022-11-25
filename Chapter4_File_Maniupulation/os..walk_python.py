import os

for (dirname, subshere, fileshere) in os.walk(r '.'):
    print('[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname))  # handle one file
