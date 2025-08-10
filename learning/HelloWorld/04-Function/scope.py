# functions are local scoped means that a variable defined in a function only exist in that function
# This can be changed by making the variable global using the global keyword (But this not recommended)

def greet(name):
    global  zsmessage
    message = 'a'


greet('Longman')

print(message)


