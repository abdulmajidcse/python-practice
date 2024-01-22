class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        return 'I\'m eating...'

class Dog(Animal):
    def about(self):
        return '{0} has four legs and it\'s {1} color.'.format(self.name, self.color)

dog = Dog('Dog', 'white')

print(dog.about())
print('The dog object is a instance of Animal class or not:', isinstance(dog, Animal))