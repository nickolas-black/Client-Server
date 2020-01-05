

import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('127.0.0.1', 53210))
serv_sock.listen(10)

client_sock, client_addr = serv_sock.accept()
#print(client_addr, client_addr)             #показывает данные подключенного склиента

while True:
    data = client_sock.recv(1024)             #если нет данных то прирываемся
    print('Что мы получили от клиента: ', data)
    if not data:
        break
    client_sock.sendall(data)


