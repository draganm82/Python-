file= open ('data.txt', 'w')        #open output file object: creates
file.write ('Hello file world!\n')  #write string verbatim

file.write('bye file world.\n') # returns number chars/bytes written
file.close()