from abc import *


class Songs(metaclass=ABCMeta):
    def __init__(self, name, dur):
        self.name = name
        self.dur = dur

    @abstractmethod
    def play(self):
        pass


class Devo(Songs):
    def __init__(self, name, dur):
        Songs.__init__(self, name, dur)  # ctor cascading

    def play(self):
        print("DEvo song %s played %s" % (self.name, self.dur))


s1 = Devo("Ganesh", 10)
s1.play()

class Jazz(Songs):
    def __init__(self,name,dur):
        Songs.__init__(self,name,dur)
    def play(self):
        print("Jazz songs %s played %s" %(self.name,self.dur))

j1 =Jazz("MJ",14)
j1.play()