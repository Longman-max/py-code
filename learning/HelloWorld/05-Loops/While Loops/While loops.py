import random

secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 1
while guess_count < 3:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry you failed")
numbers = [10, 20, 30]
total = 0
for number in numbers:
    total += number
print(f"Total:{total}")
numbers = [5,2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"The maximum number is {max}")

#using while loop only, write a program that receive four usernames and output the names of the individuals.



num = 1
while num < 4:
    if num == 1:
        user1 = input("Enter user_name: ")
    elif num == 2:
        user2 = input("Enter user_name: ")
    elif num == 3:
        user3 = input("Enter user_name: ")


    num += 1
print("User1 =", user1, "\n", "User2 =", user2, "\n", "User3 =", user3)