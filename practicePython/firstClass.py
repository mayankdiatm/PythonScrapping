#Run Time Class
#New Style Class Development
#Every class is a derived class of a "object" class
#Constructor is def __init__
#Destructor is def __def__
#this pointer in python is renamed as - "self"
#Information - object creation in Python is 2 phased object creation

class Circle:
   def __init__(self,radius=0):  #ctor
     print("Ctor called")
     self.__radius=radius

   def __del__(self):            #dtor
     print("Dtor called")

   def show(self):
     print("Radius = ",self.__radius)


cob1 = Circle()
cob2 = Circle(2.5)
#print("COB1 radius = ",cob1.radius)
#print("COB2 radius = ",cob2.radius)
cob1.show()
cob2.show()
