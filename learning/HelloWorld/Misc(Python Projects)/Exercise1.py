print("Exam remark calculator")
print("**********************")
userscore = int(input("Enter score: "))
if userscore >= 80:
    if userscore>100:
        print("Number should not exceed 100")
    else:
        print("Grade is A+")
        print("Student's remark: Nice result keep it up")
        print("The student is bright")
elif userscore >= 70:
    print("Grade is B+")
    print("Student's remark: Keep it up and put more effort")
    print("The student is bright")
elif userscore >= 60:
    print("Grade is B")
    print("Student's remark: Nice result keep it up")
    print("The student is bright")
elif userscore >= 50:
    print("Grade is C+")
    print("Student's remark: Put more effort")
    print("The student plays alot")
elif userscore >= 40:
    print("Grade is C")
    print("Student's remark: Put more effort")
    print("The student plays alot")
elif userscore >= 30:
    print("Grade is F")
    print("Student's remark: Sit up")
    print("The student is always playing in class, therefore he will repeat the class")

else:
    print("INVALID")
    first = 'John'
    last = 'Smith'
    message = first + ' [' + last + '] ''is a coder'
    msg = f'{first} [{last}] is a coder'
    print(msg)
