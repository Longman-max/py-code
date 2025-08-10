def begin():
    print("<<<ENTRANCE EXAM>>>")
    name = input("Enter your name: ")
    reg_number = input("Enter registration number: ")
    print(name + " answer all questions correctly!")
    print("The questions will be marked in real time")
    print('#To go to next question type "N"\n#To go to retry type "R"')
    ques1()
    ans2 = input("Next(N)/Retry(R): ").lower()
    if ans2 == "n":
        ques2()
        ans3 = input("Next(N)/Retry(R): ").lower()
        if ans3 == "n":
            ques3()
            ans4 = input("Next(N)/Retry(R): ").lower()
            if ans4 == "n":
                ques3()
            elif ans4 == "r":
                ques2()
            else:
                print("Error")
        elif ans3 == "r":
            ques2()
        else:
            print("Error")
    elif ans2 == "r":
        ques1()
    else:
        print("Error")


   


def ques1():
    score = 0
    print('''
1. What is the square root of 64
(a) 8
(b) 6
(c) 3
(d) 4    
    ''')
    ans1 = input("Ans: ").lower()
    if ans1 == "a":
        print("Correct")
        score += 10
    else:
        print("Fail")

def ques2():
    score = 0
    print('''
2. How many years complete a decade.
(a) 10
(b) 5
(c) 20
(d) 15
    ''')
    ans1 = input("Ans: ").lower()
    if ans1 == "a":
        print("Correct")
        score += 10
    else:
        print("Fail")

def ques3():
    score = 0
    print('''
3. The opposite of 7 is?
(a) 46
(b) 48
(c) 49
(d) 44 
    ''')
    ans1 = input("Ans: ").lower()
    if ans1 == "c":
        print("Correct")
        score += 10
    else:
        print("Fail")

begin()
