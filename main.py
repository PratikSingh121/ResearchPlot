from langchain.output_parsers import CommaSeparatedListOutputParser
#app
from app.prompt_templates import GetPromptTemplates
from app.question_framing import QuestionFraming
#package
from packages.chains import Chains

# Getting Topic
topic = input("Enter the topic. You can add just a keyword or a desciption. \nTopic : > ")

#Objects
Chain = Chains()
PromptTemplate = GetPromptTemplates(topic)
QuestionParser = CommaSeparatedListOutputParser()

# Getting Questions
questions_allowed = input("Do you want to answer questions? (y/n) \nAnswer : > ")
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

# Getting Research Data
ResearchData = Chain.chain(PromptTemplate = ResearchPrompt)

# Getting Mermaid Flowchart
MermaidPrompt = PromptTemplate.MermaidPromptTemplate(ResearchData)
MermaidFlowchart = Chain.chain(PromptTemplate = MermaidPrompt)

with open('mermaid.txt', 'w') as f:
    f.write(MermaidFlowchart)
