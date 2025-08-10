class Robot:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight

    def introduce_self(self):
        print(f"{self.name}, is {self.colour} and weighs {self.weight}kg.")


r1 = Robot('Rex', 'red', '58')
r1.introduce_self()

r2 = Robot('Optimus', 'white', '60')
r2.introduce_self()
# There has to be a new line at the end of a file in a python file according to the PEP8 standard

# There has to be double line space at the end of the end of a function
