#Usage of __new__ and how it invokes __init__

class sample:

   def __new__(cls,*args,**kwargs):
     print("NEW CALLED.......")
     return super().__new__(cls,*args,**kwargs)

   def __init__(self):
     print("INIT CALLLED......")

   def __del__(self):
     print("DEL called......")


s1 = sample()