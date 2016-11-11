#use case of getaatr,setattr,delaatr

a1='hello'
a2='world'
a3='of'
a4='unix'
a5='data'
a6='hai'

name="a"
for i in range(1,6):
  varname = name+str(i)
  print(eval(varname))  # or exec


####### Another Example

class Host:
  def __init__(self,name):
   self.name = name
  def connect(self):
   print("Connected to host")
  def auth(self):
   print("Auth user")
  def send(self):
   print("Sent data")
  def recv(self):
   print("Recvd data ")
  def close(self):
   print("Closed connection")

h1 = Host("localhost")
print(getattr(h1,"name"))  # h1.name

fnsList = ["connect","auth","recv","close"]
for fnname in fnsList:
   getattr(h1,fnname)()