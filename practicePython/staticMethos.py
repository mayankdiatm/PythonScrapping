#is a function
#accessible via CLASSNAME
#there is no arguments to it bt default

class Emps:

  __count=0   # private static variable
  total=0     # public static variable

  def __init__(self,name=0,dept=0,salary=10):
    self.name = name
    self.dept = dept
    self.salary = salary
    Emps.__count+=1
    Emps.total+=self.salary

  @classmethod
  def showtotal(cls):
    print("Total = ",cls.total)

  @staticmethod
  def showcount():
    print("Count = ",Emps.__count)


Emps.showcount()
e1 = Emps()
e2 = Emps()
e3 = Emps()
e4 = Emps()

e1.showtotal()
Emps.showcount()
