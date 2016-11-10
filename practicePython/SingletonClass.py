#SINGLETON PATTERN
#this class can have only one object in the lifetime
#if the user tries to create a second object immediately  program should exit

#BORG PATTERN
#this class can have only one object in the lifetime
#if the user tries to create a second object return same objects address -- continue program


class SingleTon:
 count=0
 def __init__(self):
   if SingleTon.count==0:
     print("Obj created")
     SingleTon.count+=1
   else:
     raise Exception("Object already exists.....")
 def show(self):
   print("Hello")

s1 = SingleTon()
s1.show()

s2 = SingleTon()  # throw an Exception / Exit program