from twisted.internet import reactor, protocol as p

class Echo(p.Protocol):
    def dataReceived(self, data):
        self.transport.write(data.upper())

class EchoFactory(p.Factory):
    def buildProtocol(self, addr):
        print('Connection by', addr)
        return Echo()

reactor.listenTCP(5007, EchoFactory())
reactor.run()


####### Client program

import socket

ip = "10.103.0.134"
port = 5007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))


s.send(b"Hello world")
res = s.recv(1024)
print(res)
s.close()