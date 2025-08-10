class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Every function in a class takes a self argument
    def move(self):
        print('move')

    def draw(self):
        print('draw')


# point = Point(10, 20)
# print(point.x)
#
# point.move()
# coordinates

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person('John Smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()


# Inheritance

class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass


dog1 = Dog()
dog1.walk()
