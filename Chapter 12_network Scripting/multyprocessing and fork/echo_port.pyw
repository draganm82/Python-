from socket import*
sock = socket (AF_INET, SOCK_STREAM)
sock.connect(('pop.secureserver.net',110)) # talk to POP email server
print (sock.recv(70))
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('learning-python.com', 21)) # talk to FTP server
print(sock.recv(70))
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect  (('http:\\www.python.net', 80)) # talk to Python's HTTP server

socket.send(b'GET/\r\n')  # fetch root page reply

print(sock.recv(70))
socket.close()