print('******LOGIN MENU******')
name = input("Enter username: ")
password = "9judgeship"
enter_password = ""
trial = 0
limit = 3
try_again = 1
again = 3
out_of_trial = False
while enter_password != password and not out_of_trial:
    if trial < limit:
        enter_password = input("Enter password: ")
        if enter_password != password:
            if try_again < again:
                print("Password not correct!, try again")
                try_again += 1
        trial += 1
    else:
        out_of_trial = True
if out_of_trial:
    print("Too many attempts, try again later.")
else:
    print("Logging in.....")
    print("Welcome back " + name)

