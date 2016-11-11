import logging

logging.basicConfig(filename="e.log")

def wrapper(fname):
 def inner(*args,**kwargs):
  logging.warning(fname.__name__+" called")
  res=fname(*args,**kwargs)
  logging.warning(fname.__name__+" exit")
  return res
 return inner

@wrapper
def some(a,b,c,d):
 print("Some called")

@wrapper
def add(a,b):
 print(a+b)

@wrapper
def minus(a,b):
 print(a-b)

@wrapper
def mult(a,b):
 print(a*b)

@wrapper
def div(a,b):
 print(a/b)
##############first.py
import mymath

mymath.add(10,20)