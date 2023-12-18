class QuestionFraming:
    def __init__(self, question: list):
        self.question = question
        self.answer = []

    def ask_questions(self):
        print("Answer the following questions:  (Leave blank if no answer)")
        for i in self.question:
            print(i+ "\n > ", end="")
            answer = input()
            if answer == "":
                answer = "No answer"
            self.answer.append(answer)
        # Add more questions if needed

    def form_dictionary(self):
        dictionary = dict(zip(self.question, self.answer))
        return dictionary