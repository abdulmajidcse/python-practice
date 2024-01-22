class MyClass:
    """This is a testing purpose class"""
    i = 1234

    def __init__(self):
        self.data = [10, 20, 30]

    def f(self):
        """This is a demo method"""
        return 'Hello world!'

x = MyClass

x.name= "Abdul Majid"
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print(x.name)

print(MyClass.name)

y = MyClass()

print ("Name: {0}".format(y.name))

for _ in range(3):
    print("---------------------------------------------------------------------") 


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)