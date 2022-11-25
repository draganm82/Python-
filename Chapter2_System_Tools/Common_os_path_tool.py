import os

print( os.path.isdir(r 'C:\\User'), os.path.isfile(r'C:\Users')
os.path.isdir(r 'C:\\config.sys'), os.path.isfile(r'C:\config.sys')
os.path.isdir(r 'nonesuch'), os.path.isfile(r'nonesuch')
os.path.exist(r 'c:\\Users\draga')
os.path.exists (r 'C:\\User\Public')
os.path.getsize(r 'C:\\autoexec.bat')

os.path.split(r'C:\temp\data.txt')

os.path.join(r'C:\temp', 'output.txt')

name = r'C:\temp\data.txt' # Windows paths
os.path.dirname(name), os.path.basename(name)
name = '/home/lutz/temp/data.txt' # Unix-style paths
os.path.dirname(name), os.path.basename(name)
os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw')


os.chdir(r'C:\Users')
os.getcwd()

os.path.abspath('') # empty string means the cwd

os.path.abspath('temp') # expand to full pathname in cwd

os.path.abspath(r'PP4E\dev') # partial paths relative to cwd

 os.path.abspath('.') # relative path syntax expanded

os.path.abspath('..')

os.path.abspath(r'..\examples')

os.path.abspath(r'C:\PP4thEd\chapters') # absolute paths unchanged

os.path.abspath(r'C:\temp\spam.txt')

# we can start program with this command
  
os.startfile("webpage.html") # open file in your web browser
os.startfile("document.doc") # open file in Microsoft Word
os.startfile("myscript.py") # run file with Python