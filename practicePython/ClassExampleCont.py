class Emp:
  def __init__(self,name,dept,sal): # ctor
    self.name = name
    self.dept = dept
    self.sal  = sal
  def __str__(self):   #overriding to string
    return "(%s,%s,%s)" %(self.name,self.dept,self.sal)

e1 = Emp("arun","sales",15000)
e2 = Emp("ajit","sales1",18000)
print(e1)