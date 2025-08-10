import random


def shuffle_songs(playlist):
    for i in range(len(playlist)):
        j = random.randint(i, len(playlist) - 1)
        playlist[i], playlist[j] = playlist[j], playlist[i]
    print(playlist)


def play_default(playlist):
    print(playlist)


def play_music():
    focus_code_hits = ['Goodbyes', 'Go Flex', 'White Iverson', 'Laugh it Off', 'Congratulations']
    while True:
        prompt = input("Do you want to shuffle? Yes or No: ")
        if prompt.upper() == 'YES':
            shuffle_songs(focus_code_hits)
        elif prompt.upper() == "NO":
            play_default(focus_code_hits)
        else:
            print('Incorrect format')


play_music()
