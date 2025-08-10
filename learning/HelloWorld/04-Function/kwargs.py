def save_user(**user):
    print(user)


# when we use double asterisk we can pass multiple keyword arguments
save_user(id=1, name='John', age=22)
save_user(id=2, name='Mark', age=23)
