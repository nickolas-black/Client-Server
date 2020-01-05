



import socket

clinet_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clinet_sock.connect(('127.0.0.1', 53210))
clinet_sock.sendall(b'Hello, word')
data = clinet_sock.recv(1024)
clinet_sock.close()
print('Получили ', repr(data))



