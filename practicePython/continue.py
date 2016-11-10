class MyArray:
  def __init__(self):
    self.data = []

  def Add(self,value):
    if value % 2 ==0:
      self.data.append(value)
    else:
      print("Input is INVALID shld be EVEN.....")

  def __eq__(self, other):
      if self.data == other.data:
          return True
      else:
          return False
  def show(self):
    print("Vals = ",self.data)

a1 = MyArray()
a1.Add(10)    # supports EVEN nos
a1.Add(20)
a2 = MyArray()
a2.Add(10)
a2.Add(20)
a1.show()
a2.show()
if a1 == a2:
  print("yes they are equal")
else:
  print("no they are NOT equal")