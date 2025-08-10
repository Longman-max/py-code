#getting input from user:
color = input("Enter a color: ")
plural_noun = input("Enter a Plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love you " + celebrity)
#list and list methods
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tobi"]
friends2 = friends.copy( )
print(lucky_numbers)
#defining functions
def say_hi(name, age):
    print("Hello " + name + " you are " + str(age))

say_hi("Rita", 16)
say_hi("Mosh", 35)
#using funtions to find the cube of a value
def cube(num):
    return num*num*num

result = cube(4)
print(result)

#using functions to calculte the maximum number in a function
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))
#bulding a better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
#dictionaries
month_conversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(month_conversions.get("Jan"))
#while loops
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter word: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of guesses, You lose!")
else:
    print("You won")
print('ENTER NAME AND PASSWORD TO LOGIN')
name = input("Enter username: ")
password = "9judgeship"
enter_password = ""
trial = 0
limit = 3

out_of_trial = False
while enter_password != password and not out_of_trial:
    if trial < limit:
        enter_password = input("Enter password: ")
        print("Try again")
        trial += 1
    else:
        out_of_trial = True
if out_of_trial:
    print("Sorry u are out of trials.")
else:
    (print("Welcome back " + name))

#mistake
name = input("Enter username: ")
password = "9judgeship"
enter_password = ""
trial = 0
limit = 3
try_again = 1
out_of_trial = False
while enter_password != password and not out_of_trial:
    if trial < limit:
        enter_password = input("Enter password: ")
        if try_again < limit:
            try_again += 1
        else:
            break
        trial += 1
    else:
        out_of_trial = True
if out_of_trial:
    print("Sorry u are out of trials.")
    print("Try again")
else:
    (print("Welcome back " + name))

def raise_to_power(base_num, power):
    result = 1
    for index in range(power):
        result = result * base_num
    return result

print(raise_to_power(3, 2))
#2d list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0
     ]
]
for row in number_grid:
    for col in row:
        print(col)