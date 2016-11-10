from multiprocessing import Process,Pool
from threading import Thread
import os
import time

def job1(x):
  print("JOB1 = PID = ",os.getpid(),)
  print("JOB1 = ",x)
  time.sleep(2)

# this check is compulsory for all multiprocessing
# execution
if __name__  == "__main__":
  arr = [(1,1),(2,2),(3,3),(4,4),5,6,7,8,9,10]
  p = Pool(10)
  start = time.time()
  p.map(job1,arr)
  p.close()
  end = time.time()
  print("Time taken = ",end-start)