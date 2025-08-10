#
# name = input("your name ?")
# if name.endswith("ict"):
#     print("you are good to go")
# else:
#     print("not allow to go")
#
# number = int(input("Enter a number"))
# if number % 2 ==0:
#     print("{} is an even number".format(number))
# else:
#     print("{} is an odd number".format(number))
#
# enter = int(input("enter a digit but not less than 0"))
# while enter < 0 :
#     enter = int(input("enter a digit but not less than 0"))

# counta = 0
#
# while counta <= 12:
#     countb = 1
#     while countb <= 12:
#         print(f'{counta} *  {countb}  =  {counta * countb}')
#         countb = countb + 1
#     print(" ")
#     counta = counta + 1
#

import sys
import turtle

ninja = turtle.Turtle()
ninja.speed(5000)
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    ninja.right(2)
turtle.done()



if sys.platform == "win32":
    print("You are using a window operating system thanks")
    
