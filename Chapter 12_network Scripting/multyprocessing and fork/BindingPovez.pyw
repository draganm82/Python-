from socket import *
sock = socket(AF_INET, SOCK_STREAM) # try to bind web port on general server
sock.bind(('http://www.google.com', 80)) # learning-python.com is a shared machine

sock.send(b'GET/\r\n')

print (sock.recv(70))

sock.close()