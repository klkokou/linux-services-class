from datetime import datetime
import socket


def get_datetime_str(now:datetime):
    str = now.strftime("%d") + '.'
    str+= now.strftime("%m") + '.'
    str+=now.strftime("%Y") + ' '
    str+=now.strftime("%H")+':'
    str+=now.strftime("%M")    
    return str



sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket was created")
port = 1303
sock.bind(('0.0.0.0', port))
print("Socket was binded to port number:", (port))
sock.listen()
print("Socket is listening")

while True:
    print("Waiting for connection")
    conn, addr = sock.accept()
    print("Got connection from:", addr)
    date_time = get_datetime_str(datetime.now())
    new = date_time.encode("ascii")
    conn.send(new)
    conn.close()
    print("Connection closed:", addr)


