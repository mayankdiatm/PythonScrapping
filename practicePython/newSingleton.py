# Singleton
# this class can have only one object in the lifetime
# if the user tries to create a second object
# immdlty program shld exit

# Borg pattern
# this class can have only one object in the lifetime
# if the user tries to create a second object
# return same objects address - continue program

class SingleTon1:
    count = 0

    def __init__(self):
        if SingleTon1.count == 0:
            print("Obj created")
            SingleTon1.count += 1
        else:
            raise Exception("Object already exists.....")

    def show(self):
        print("Hello")


s1 = SingleTon1()
s1.show()


# s2 = SingleTon1()  # throw an Exception / Exit program



class Singleton:
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *a, **k)
        return cls._inst

    def fun(self):
        print("Fun...")


s = Singleton()
s.fun()

s1 = Singleton()
s1.fun()

print(id(s))
print(id(s1))

