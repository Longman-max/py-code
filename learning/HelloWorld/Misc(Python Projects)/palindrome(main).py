def is_palindrome(user_word):
    return user_word.lower() == user_word.lower()[::-1]


while True:
    word = input('Enter a word: ')
    converted = word.lower().capitalize()
    if is_palindrome(word):
        print(f'{converted} is a palindrome')
    else:
        print(f'{converted} is not a palindrome')
