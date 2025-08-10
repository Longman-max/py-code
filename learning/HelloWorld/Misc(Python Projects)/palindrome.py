print("<<<<Max number checker>>>>")


def max_n(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1, "is the greatest number.")
        return num1
    elif num2 > num1 and num2 > num3:
        print(num2, "is the greatest number.")
        return num2
    elif num3 > num1 and num3 > num2:
        print(num3, "is the greatest number.")
        return num3
    else:
        print("Numbers are equal")


num1 = input("Value: ")
num2 = input("Value: ")
num3 = input("Value: ")
max_n(num1, num2, num3)


def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Compare the original word with its reverse
    return word == word[::-1]


# Test the function
input_word = input("Enter a word or phrase: ")
if is_palindrome(input_word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")


def sentence(phrase):
    phrase = input("Enter a word: ")
    if " " in phrase:
        print("Remove space")


sentence('')
