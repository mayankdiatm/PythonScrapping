class MyArray:
    count = -1

    def __init__(self):
        self.data = []

    def Add(self, value):
        self.data.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        if MyArray.count < len(self.data) - 1:
            MyArray.count += 1
            return self.data[MyArray.count]
        else:
            raise StopIteration()


a1 = MyArray()
a1.Add(10)
a1.Add(20)
a1.Add(30)
a1.Add(40)
a1.Add(50)

for i in a1:  # __iter__  & __next__
    print(i)
