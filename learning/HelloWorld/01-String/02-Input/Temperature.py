temperature = 25

if temperature > 30:  #used for a conditional statement
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 50: #elif means else if it is ysed is the previous conditions  were not true, then try this condition.
    print("Its a nice day")
elif temperature > 10:
    print("Its a bit cold")
else:
    print("It's cold")
print("Done")
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit == "k" or "K":
    converted = int(weight) / 0.45
    print("Weight in Kgs: " + str(converted))
elif unit == "l" or "L":
    pounds = int(weight) * 0.45
    print("Weight in Lbs: " + str(pounds))