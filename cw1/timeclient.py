import socket

server_ip = input()
sock= socket.socket()
port = 1303
sock.connect((server_ip,port))
print(sock.recv(1024).decode())
sock.close()