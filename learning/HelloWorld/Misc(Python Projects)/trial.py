days = {
    'Mon': 'Monday',
    'Tue': 'Tuesday',
    'Wed': 'Wednesday',
    'Thu': 'Thursday',
    'Fri': 'Friday'
}

user_prompt = input('Prompt: ')
for word in user_prompt:
    for key in days:
        if word == days[key]:
            print(days[key])
        else:
            print('Not available')
