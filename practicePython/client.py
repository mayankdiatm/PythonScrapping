######## Client program

import socket

serverip = "127.0.0.1"
serverport = 12345

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverip, serverport))

    res = sock.recv(1024)

    print(res.decode("utf-8"))
    sock.close()
except Exception as e:
    print(e)