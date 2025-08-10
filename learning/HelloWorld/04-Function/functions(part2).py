def disp(string):
    print(string)

def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")

print("Start")
greet_user("John")
print("Finish")

# we can also pass multiple arguments to a function eg
def greetings(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")

greetings("John", "Mark")
