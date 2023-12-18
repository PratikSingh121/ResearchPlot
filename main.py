from langchain.output_parsers import CommaSeparatedListOutputParser
#app
from app.prompt_templates import GetPromptTemplates
from app.question_framing import QuestionFraming
#package
from packages.chains import Chains

# Getting Topic
print('\033[93m' + "Enter the topic. You can add just a keyword or a desciption.\nTopic : > " + '\033[0m', end="")
topic = input()

#Objects
Chain = Chains()
PromptTemplate = GetPromptTemplates(topic)
QuestionParser = CommaSeparatedListOutputParser()

# Getting Questions
# print in green color

print('\033[92m' + "Do you want to answer some questions? (y/n) \nAnswer : > " + '\033[0m', end="")
questions_allowed = input()
print()

if questions_allowed == 'y':
    questions_allowed = True
else:
    questions_allowed = False

if questions_allowed:
    QuestionsList = Chain.chain(PromptTemplate = PromptTemplate.QuestionPromptTemplate(), parser = QuestionParser)
    questionframing = QuestionFraming(QuestionsList)
    questionframing.ask_questions()
    questions = questionframing.form_dictionary()

    # convert questions dictionary to string in format of - Ques. key \n Ans. value
    questions = '\n'.join([f'Ques. {key} \n Ans. {value}' for key, value in questions.items()])

    ResearchPrompt = PromptTemplate.ResearchPromptTemplate(questions)
else:
    ResearchPrompt = PromptTemplate.ResearchPromptTemplate()

#print a brown line
print('\033[93m' + "------------------------------------------------------------------------------------------------------------------------" + '\033[0m')

# Getting Research Data
print('\033[92m' + "Researching based on your usecase 📚\n" + '\033[0m')
ResearchData = Chain.chain(PromptTemplate = ResearchPrompt)
#print research completed in ligher green color and emogi
print('\033[92m' + "Research completed ✅\n" + '\033[0m')

print('\033[93m' + "------------------------------------------------------------------------------------------------------------------------" + '\033[0m')

# Getting Mermaid Flowchart
print('\033[92m' + "Generating Mermaid Flowchart 📊\n" + '\033[0m')
MermaidPrompt = PromptTemplate.MermaidPromptTemplate(ResearchData)
MermaidFlowchart = Chain.chain(PromptTemplate = MermaidPrompt)
#print mermaid flowchart generated in ligher green color and emogi
print('\033[92m' + "Mermaid Flowchart generated ✅\n" + '\033[0m')

print('\033[93m' + "------------------------------------------------------------------------------------------------------------------------" + '\033[0m')

with open('mermaid.txt', 'w') as f:
    f.write(MermaidFlowchart)

print('\033[92m' + "Mermaid Flowchart saved in mermaid.txt ✅\n" + '\033[0m')