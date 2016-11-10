class Emp:
  def __init__(self,name,dept,sal): # ctor
    self.name = name
    self.dept = dept
    self.sal  = sal
  def __eq__(self,other):
    print("Hey i am here....")
    print("SELF = ",self.__dict__)
    print("OTHER= ",other.__dict__)
    if self.dept == other.dept:
     return True
    else:
     return False



e1 = Emp("arun","sales",15000)
e2 = Emp("ajit","sales1",18000)

if e1==e2:  # Emp.__eq__(e1,e2)
  print("yes....")
else:
  print("no.....")