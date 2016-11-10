from multiprocessing import Process
import os
import time

def job1():
    print("JOB1 = PID = " , os.getpid())
    time.sleep(5)

def job2():
    print("JOB2 = PID = " , os.getpid())
    time.sleep(10)

#this check is compulsory for all multiprocessing execution
if __name__ =="__main__":
    print("Monitor PID = ",os.getpid())
    p1 = Process(target=job1,args=())
    p2 = Process(target=job2, args=())
    p1.daemon=True #this will be  BACKGROUND Process #boolean flag and must be set before start() is called
    p2.daemon=True
    p1.start()
    p2.start()
    start = time.time()
    p1.join()
    p2.join()
    end = time.time()
    print("Total Time taken",end-start)