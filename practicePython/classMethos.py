#is a bound Method
#is accessible via Object
# by default first arg will be "CLASNAME"
class sample:
    def __init__(self):
        pass

    def show(self):
        pass

    @classmethod
    def fun1(cls):
        pass

    @staticmethod
    def fun2():
        pass


s1 = sample()

print(s1.show)
print(s1.fun1)
print(sample.fun2)