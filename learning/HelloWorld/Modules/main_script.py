from my_module import *
from formular_module import *
import random

random_number = random.randint(1, 20)
print(random_number)

print(find_max([5, 10, 45, 6]))


dog = Dog()
dog.walk()

shape = Formula(5, 6)
print(shape.rec_perimeter())
print('Hello world'.center(50  , '*'))