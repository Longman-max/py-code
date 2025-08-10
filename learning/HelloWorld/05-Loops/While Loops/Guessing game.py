secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You lose!")


import random
secret_number = random.randint(1, 10)
def start():
    print('***GUESSING GAME***')
    guess = 1
    guess_limit = 3
    trials = 3
    while guess <= guess_limit:
        guess += 1
        user_guess = int(input('Guess a number > '))
        if user_guess == secret_number:
            print('You won!')
            break
        else:
            trials -= 1
            print(f'You have {trials} trials left')
            if trials == 0:


The secret number was {secret_number}
import random
def start():
    print('***GUESSING GAME***')
    secret_number = random.randint(1, 10)
    guess_limit = 3
    trials = 0
    while trials < guess_limit:
        user_guess = int(input('Guess a number > '))
        if user_guess == secret_number:
            print('You won!')
            break
        else:
            trials += 1
            print('Sorry incorrect')
            print(f'You have {guess_limit - trials} trials left')
    if trials == guess_limit and user_guess != secret_number:
        print(f'The secret number was {secret_number}')