successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break
# The code in the else block will run as long as the loop did not
# have an early termination
else:
    print('Attempted 3 times and failed')