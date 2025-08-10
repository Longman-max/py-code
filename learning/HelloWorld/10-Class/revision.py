class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'I am {self.name}')

    def tell_age(self):
        print(f'I am {self.age} years old')


john = Person('Andrew', 18)
john.tell_age()


