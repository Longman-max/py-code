mass = int(input("Mass: "))
unit = input("(Kg)s or (Lb)s: ")

if unit.upper() == "KG":
    converted = mass / 0.45
    print("Weight in kgs: " + str(converted))
elif unit.upper() == "LB":
    pounds = mass * 0.45
    print("Weight in lbs: " + str(pounds))
else:
    print("INVALID")

for num in range(1, 30, 2):
    print(num)
value = int(input("Enter temperature: "))
unit = input("Enter C or K: ")

if unit.upper() == "C":
    converted = 273 - value
    print("Celuis to kelvin is: " + str(converted))
elif unit.upper() == "K":
    converted = 273 + value
    print("kelvin to Celuis  is: " + str(converted))
else:
    print("Error")

