# TODO: Add comments to this file

# A string is written with a single or double quote
'Hello world'

# Variables can containers used to store values (strings, numbers, boolean)
name = 'John'
age = 35
# Variables can be changed.
name = 'Longman'
age = 17

age = input("Enter year of birth: ")
print(age)
print (2023 - int(age))
name = input("Enter your name: ")
print("Welcome " + name )
First = input("Enter first number: ")
Second = input("Enter second number: ")
sum = int(First) + int(Second)
print(sum)
course = "Python for beginners"
print(course.upper())
print(course.replace("y" , "2"))
print(course.find("g"))
print(course.lower())
print("Hippo" in course)
fact = "Hippotamus is a wild animal"
print(fact.upper())
print("Did you know that "  + fact)

# To get the index position of a string
print(fact.find('m'))
print(fact.replace('wild' , 'tame'))
print("Python" in fact)
print(3 + 5)
print(10 * 3)
print(10 ** 3)
print(10 / 3)
print(10 % 3)


# String method

course = ("Python for begineers")
print(course.upper())
print(course.find("y"))
print("y" in course)
print(course.replace("y" , "3"))
print(course.lower())
print(len(course))
