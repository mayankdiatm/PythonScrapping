##### Server program
import socket
import time

ip1 = socket.gethostbyname("localhost")
ip2 = socket.gethostname()
port = 12345

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sock)
    sock.bind((ip1, port))
    print(sock)
    sock.listen(5)
    while True:
        client, name = sock.accept()
        print("Hey got the conn from ", name)
        time.sleep(10)
        client.send(b"Today breaking newsss....")
        client.close()
except Exception as e:
    print(e)
