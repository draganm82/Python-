from io import StringIO
import sys

buff = StringIO()
buff.write('spam\n')

buff.write('eggs\n')

buff.getvalue()

buff = StringIO('ham\nspam\n')  #provide input from string
buff.readline()