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


class Jazz(Songs):
    def __init__(self, name, dur):
        Songs.__init__(self, name, dur)  # ctor cascading

    def play(self):
        print("JAZZ song %s played %s" % (self.name, self.dur))


class Rock(Songs):
    def __init__(self, name, dur):
        Songs.__init__(self, name, dur)  # ctor cascading

    def play(self):
        print("ROCK song %s played %s" % (self.name, self.dur))


class Inst(Songs):
    def __init__(self, name, dur):
        Songs.__init__(self, name, dur)  # ctor cascading

    def play(self):
        print("INST song %s played %s" % (self.name, self.dur))


s1 = Devo("Ganesh", 10)
j1 = Jazz("ABC", 20)
r1 = Rock("PQR", 10)
i1 = Inst("XYZ", 10)

for songob in (s1, j1, r1, i1):
    songob.play()








