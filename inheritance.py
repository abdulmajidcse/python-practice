class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        return 'I\'m eating...'


class Animal_Food:
    def __init__(self, food_name):
        self.food_name = food_name
    
    def get_food(self):
        return self.food_name


class Cat(Animal, Animal_Food):
    def __init__(self, name, color, food_name):
        Animal.__init__(self, name, color)
        Animal_Food.__init__(self, food_name)

    def about(self):
        return '{0} has four legs and it\'s {1} color.'.format(self.name, self.color)


cat = Cat('Mina', 'white', 'Milk')

print(cat.name, 'is eating ', cat.get_food())

print('--------------------------------------------')

print(cat.about())

print('---------------------------------------')

print('The', cat.name, 'object is a instance of Animal class or not:', isinstance(cat, Animal))