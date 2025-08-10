def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


class Mammal():
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass


