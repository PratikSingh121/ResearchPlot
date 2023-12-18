class QuestionFraming:
    def __init__(self, question: list):
        self.question = question
        self.answer = []

    def ask_questions(self):
        print('\033[91m' + "Answer the following questions:  (Leave blank if no answer)" + '\033[0m')
        for i in self.question:
            # print in blue color
            print('\033[94m' + i + "\n > " + '\033[0m', end="")
            answer = input()
            if answer == "":
                answer = "No answer"
            self.answer.append(answer)
        # Add more questions if needed

    def format_information(self):
        information = dict(zip(self.question, self.answer))
        return information