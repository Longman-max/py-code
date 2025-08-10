class EntranceExam:
    def _init_(self):
        self.questions = [
            {
                'question': 'What is the square root of 64?',
                'options': {
                    'a': '8',
                    'b': '6',
                    'c': '3',
                    'd': '4'
                },
                'answer': 'a'
            },
            {
                'question': 'How many years complete a decade?',
                'options': {
                    'a': '10',
                    'b': '5',
                    'c': '20',
                    'd': '15'
                },
                'answer': 'a'
            },
            {
                'question': 'The opposite of 7 is?',
                'options': {
                    'a': '46',
                    'b': '48',
                    'c': '49',
                    'd': '44'
                },
                'answer': 'c'
            }
        ]

    def display_question(self, question_dict):
        print(question_dict['question'])
        for option, value in question_dict['options'].items():
            print(f"({option}) {value}")

    def begin(self):
        print("<<<ENTRANCE EXAM>>>")
        name = input("Enter your name: ")
        reg_number = input("Enter registration number: ")
        print(name + " answer all questions correctly!")
        print("The questions will be marked in real-time")
        print('#To go to the next question type "N"\n#To retry the current question type "R"')

        score = 0

        for i, question in enumerate(self.questions):
            self.display_question(question)
            ans = input("Ans: ").lower()

            while ans not in ['a', 'b', 'c', 'd', 'n', 'r']:
                print("Invalid input. Please try again.")
                ans = input("Ans: ").lower()

            if ans == 'n':
                continue
            elif ans == 'r':
                while ans == 'r':
                    self.display_question(question)
                    ans = input("Ans: ").lower()
            elif ans == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is", question['options'][question['answer']])

        print("Exam Finished!")
        print("Total score:", score, "out of", len(self.questions))

if __name__ == "_main_":
    exam = EntranceExam()
    exam.begin()
