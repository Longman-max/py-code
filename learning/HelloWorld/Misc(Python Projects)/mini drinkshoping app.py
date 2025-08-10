def begin():
    while True:
        print("Do you want to continue or begin")
        select2 = input("Yes/No: ").lower()
        if select2 == "yes":
            item()

def  item():
    print("Select any of the characters which represent the item below;")
    print('''
Fanta = F
Coke = K
Sprite = S
Chocolate = C
    ''')
    select = input("Select item: ").lower()
    if select == "f":
        fanta()
    elif select == "k":
        coke()
    elif select == "s":
        sprite()
    elif select == "c":
        chocolate()
    else:
        error()

def fanta():
    print("You have chosen Fanta: ")
    p = int(input("Enter the prize of Fanta: "))
    a = int(input("Enter the amount bought: "))
    tot = (p * a)
    print(f"You are to pay {tot} CFA")

def coke():
    print("You have chosen Coke: ")
    p = int(input("Enter the prize of Coke: "))
    a = int(input("Enter the amount bought: "))
    tot = (p * a)
    print(f"You are to pay {tot} CFA")

def sprite():
    print("You have chosen sprite: ")
    p = int(input("Enter the prize of sprite: "))
    a = int(input("Enter the amount bought: "))
    tot = (p * a)
    print(f"You are to pay {tot} CFA")

def chocolate():
    print("You have chosen chocolate: ")
    p = int(input("Enter the prize of chocolate: "))
    a = int(input("Enter the amount bought: "))
    tot = (p * a)
    print(f"You are to pay {tot} CFA")

def error():
    print("You have entered and invalid key")

begin()
