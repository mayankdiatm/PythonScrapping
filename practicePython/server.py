import socket
import time
from threading import Thread
from multiprocessing import Process

ip1 = socket.gethostbyname("localhost")
ip2 = socket.gethostname()
#ip1 = "10.103.0.134"
port = 12340

def job1(client,name):
   print("Hey got the conn from ",name)
   time.sleep(10)
   client.send(b"Today breaking newsss....")
   print(name,"got closed")
   client.close()

if __name__ == '__main__':
 try:
     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     sock.bind((ip1,port))
     sock.listen(5)
     while True:
       client,name  = sock.accept()
       t = Process(target=job1,args=(client,name))
       t.start()
 except Exception as e:
     print(e)