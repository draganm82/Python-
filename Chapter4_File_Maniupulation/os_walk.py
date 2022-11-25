import os
matches = []
for (dirname, dirshere, fileshere) in os.walk(r'C:'):
    for filename in fileshere:
        if filename.endswith('.py'):
            pathname = os.path.join(dirname, filename)
            if 'mimetypes' in open(pathname).read():
                matches.append(pathname)

for name in matches: print(name)