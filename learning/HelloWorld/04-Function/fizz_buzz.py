def fizz_buzz(input):
    # Always move the condition that is more specific to the top.
    # TODO: Try upgrading the algoritmn
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'

    return input


print(fizz_buzz(4))
print(fizz_buzz(5))
print(fizz_buzz(3))
print(fizz_buzz(15))
