print("*****Login Page****")

def login():
    trial = 0
    trial_limit = 4
    while trial < trial_limit:
        trial += 1
        password = input("Set password: ")
        user_password = input("Enter password to login: ")
        if password == user_password:
            print("You have been logged in..")
            trial = trial_limit
        else:
            print(f'You have {trial} trials left!')
            

    
def reset():
    print("Do you want to reset password?")
    select = input("Yes/No").lower()
    if select == "Yes":
        print("Password changed")



login()