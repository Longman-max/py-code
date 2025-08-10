balance = 0
while True:
    print('    Banking app    ')
    print('*'*20)
    print('''
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
''')
    print('*'*20)
    user = int(input('Select: '))
    if user == 1:
        print('Balance: ', balance)
    elif user == 2:
        deposit = int(input('Amount to deposit: '))
        balance += deposit
    elif user == 3:
        expense = int(input('Amount to be withdrawn: '))
        if expense > balance:
            print('Insufficient balance!')
        else:
            balance -= expense
    elif user == 4:
        print('Bye!')
        break
    