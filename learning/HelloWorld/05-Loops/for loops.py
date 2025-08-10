numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) #we use loops run a list line by line

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1 #similar to loops but longer
#Range
numbers = range(5, 10)
for value in numbers:
    print(value)
#We dont relly ned to store each number in a variable:
for value in range(5):
    print(value)
#Tuples
num = (1, 2, 3, 3,3)
print (num.count(3))

numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total += number
print(f"Total: {total}")
#using for loops to remove a duplicate in a list
numbers = [2, 2, 3, 3, 4, 5, 5, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#tuples
numbers = (1, 2, 3, 4, 5, 6, 7)
for item in  numbers:
    print(item)

first = int(input("Enter first number: "))
second = int(input("Enter second number"))
sum = first + second
print(sum)
#removing duplicates from an input.
numbers = input("Enter numbers: ")
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

numbers = [5, 2, 5, 2, 2]
print