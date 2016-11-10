from multiprocessing import Process
from threading import Thread
import os
import time

def job1():
    print("JOB1 == PID == ",os.getpid())
    time.sleep(5)

def job2():
    print("JOB2 == PID == ",os.getpid())
    time.sleep(5)

#this check is compulsory for all multiprocessing execution
if __name__ =="__main__":
    print("Monitor PID = ",os.getpid())
    p1 = Thread(target=job1,args=())
    p2 = Thread(target=job2, args=())
    p1.start()
    p2.start()
    start = time.time()
    p1.join()
    p2.join()
    end = time.time()
    print("Total Time taken ==", end - start)