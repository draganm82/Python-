import os

os.listdir ('.')[:4]

root = r'C:\\AMD'
for (dir, subs, files) in os.walk(root): print(dir)

root.encode()
for (dir, subs, files) in os.walk(root.encode()): print(dir)

for (dir, subs, files) in os.walk(root):
    try:
        print(dir)
    except UnicodeEncodeError:
        print (dir.encode())        # or simply punt if enocde may fail too
        