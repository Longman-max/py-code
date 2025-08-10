print("***WELCOME TO EMOJI-AI***")
while True:
    message = input(">").lower()
    words = message.split(' ')
    # split  method goes through a string and checks for a space if it sees it will return the word before it as an element of a list
    if message == '' or message == ' ':
        print("You have to give me a word!")
    else:
        emojis = {
            ":)": "😀",
            "happy": "😀",
            "glad": "😀",
            "Good morning": "Good morning 😀",

            ":(": "😢",
            "sad": "😢",
            "unhappy": "😢",
            "I am sad": "I am sad 😢",

            "laugh": "🤣🤣"
        }
        output = ""
        if message in emojis:
            for word in words:
                output += emojis.get(word, word) + " "
            print(f'"{message}" is {output}')
        else:
            print(f" Sorry *{message}* doesn't have an emoji 😢")
            print("Try again")
