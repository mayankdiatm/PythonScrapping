from multiprocessing import Process
import os
import time

class MyProcess(Process):
  def __init__(self):
    Process.__init__(self)  # super().__init() #need to call base class constructor
    self.start()

  def run(self):
    print("Job1 = ",os.getpid())
    time.sleep(2)

if __name__ == '__main__':
 p1 = MyProcess()
 p2 = MyProcess()
