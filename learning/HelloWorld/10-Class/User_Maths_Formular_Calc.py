class User:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName= lastName
    def welcome(self):
        print("Welcome {} {}".format(self.title, self.firstName ))
    def area(self):
        pi =3.142
        r = float(input("Enter a radius: "))
        A = pi * r * r

        print("{} {}".format(self.title, self.firstName) , " ,calculated area is ",A, "cm²")

    def area_square(self):
        l = float(input("Enter a length: "))
        A = l * l

        print("{} {}".format(self.title, self.firstName), " ,calculated area is ", A, "cm²")

    def area_triangle(self):
        h = float(input("Enter a height: "))
        b = float(input("Enter a base: "))
        A = 0.5 * h * b

        print("{} {}".format(self.title, self.firstName), " ,calculated area is ", A, "cm²")

    def volume_sphere(self):
        pi = 3.142
        r = float(input("Enter a radius: "))
        V = 4/3 * pi * r * r * r

        print("{} {}".format(self.title, self.firstName), " ,calculated volume is ", V, "cm³")

    def volume_of_a_cylinder(self):
        h = float(input("Enter a height: "))
        r = float(input("Enter a radius: "))
        pi = 3.142
        V = pi * pi * h * r

        print("{} {}".format(self.title, self.firstName), " ,calculated volume is ", V, "cm³")
    def user_prompt(self):
        title = input("Input your title: ")
        firstname = input("Input your First Name: ")
        lastname = input("Input your Last Name: ")

        self.title = title
        self.firstName = firstname
        self.lastName = lastname



user1 = User(" ", "", "")

print(user1.user_prompt())
print(user1.welcome())
print(user1.area())

user2 = User(" ", "", "")

print(user2.user_prompt())
print(user2.welcome())
print(user2.area_square())

user3 = User(" ", "", "")

print(user3.user_prompt())
print(user3.welcome())
print(user3.area_triangle())

user4 = User(" ", "", "")

print(user4.user_prompt())
print(user4.welcome())
print(user4.volume_sphere())

user5 = User(" ", "", "")

print(user5.user_prompt())
print(user5.welcome())
print(user5.volume_of_a_cylinder())
