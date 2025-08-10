def calc():
    print("Which of the following table do you want to use?")
    print('''
1. Addition table
2. Substraction table
3. Multiplication table
4. Division table
    ''')
    select = input("Select: ")
    if select == "1":
        addition()
    elif select == "2":
        substraction()
    elif select == "3":
        multiplication()
    elif select == "4":
        division()
    else:
        error()
        print("Do you want to continue?")
        select2 = input("Select either Yes or No: ").lower()
        if select2 == "yes":
            retry()
        elif select2 == "no":
            byebye()
        else:
            exit()
def addition():
    print("You have chosen addition")
    choice = int(input("Enter a number to get the addition table(1 to 24): "))
    value = 1
    while value <= 24:
        print(choice, "+ ", value, "=", (choice + value))
        value += 1
    retry()
def substraction():
    print("You have chosen subtraction")
    choice = int(input("Enter a number to get the substraction table(1 to 24): "))
    value = 1
    while value <= 24:
        print(value, "- ", choice, "=", (value - choice))
        value += 1
    retry()
def division():
    print("You have chosen division")
    choice = int(input("Enter a number to get the division table(1 to 24): "))
    value = 1
    while value <= 24:
        print(choice, "/ ", value, "=", (choice / value))
        value += 1
    retry()
def multiplication():
    print("You have chosen multiplication")
    choice = int(input("Enter a number to get the multiplication table(1 to 24): "))
    value = 1
    while value <= 24:
        print(choice, "x", value, "=", (value * choice))
        value += 1
    retry()
def error():
    print("Invalid selection!")

def retry():
    calc()
def byebye():
    print("Goodbye....")

calc()


