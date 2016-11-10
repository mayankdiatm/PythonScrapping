def outer(fnname):
  print("Hello")
  def inner(*args,**kwargs):
   print("Before")
   res = fnname(*args,**kwargs)
   print("After")
   return res
  return inner   # modified function

@outer
def add(a,b):
 print(a+b)
 return a+b

@outer
def minus(a,b):
 print(a-b)
 return a-b

@outer
def mult(a,b):
 print(a*b)
 return a*b

@outer
def div(a,b):
 print(a/b)
 return a/b
