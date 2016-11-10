from abc import *


class BaseProtocol(metaclass=ABCMeta):
    def __init__(self, ip=0, user=0, password=0):
        pass

    @abstractmethod
    def connect(self):
        pass

    def disconnect(self):
        pass


class HTTPProto(BaseProtocol):
    def connect(self):
        print("connected HTTP server")


h1 = HTTPProto()
h1.connect()

# derived class should comp define - abstract
# optional to redefine             - leave as it is