class MyArray:
    def __init__(self):
        self.data = []
    def Add(self,value):
        if value%2==0:
            self.data.append(value)
        else:
            print("input is invalid should be even")
    def show(self):
        print("Vals = ",self.data)


a1=MyArray()
a1.Add(10)
a1.Add(11)
a1.Add(20)
a1.Add(30)
a1.Add(40)
a1.show()