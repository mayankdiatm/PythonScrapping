class MyArray:
  def __init__(self):
    self.data = []

  def Add(self,value):
    if value % 2 ==0:
      self.data.append(value)
    else:
      print("Input is INVALID shld be EVEN.....")

  def __len__(self):
    return len(self.data)

  def show(self):
    print("Vals = ",self.data)

  def __setitem__(self,index,value):
      if index >= 0 and index < len(self.data):
          if value % 2 == 0:
              self.data[index] = value
          else:
              print("Num shld be EVEN")
      else:
          print("Invalid index")

a1 = MyArray()
a1.Add(10)    # supports EVEN nos
a1.Add(20)
a2 = MyArray()
a2.Add(10)
a2.Add(20)
a1.show()
a2.show()


print(len(a1))
a1[0] = 22 #list emulation #setitem

#getitem
#delitem