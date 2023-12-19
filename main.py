from langchain.output_parsers import CommaSeparatedListOutputParser
import subprocess
import os
#app
from app.prompt_templates import GetPromptTemplates
from app.question_framing import QuestionFraming
#package
from packages.chains import Chains

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Getting Topic
print('\033[93m' + "Enter the topic. You can add just a keyword or a description.\nTopic : > " + '\033[0m', end="")
topic = input()
print()

#Objects
Chain = Chains()
PromptTemplate = GetPromptTemplates(topic)
QuestionParser = CommaSeparatedListOutputParser()

# Getting Questions
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
    questions = questionframing.format_information()

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

# Formatting Mermaid Code
if '```mermaid' in MermaidFlowchart:
    MermaidFlowchart = MermaidFlowchart.split('```mermaid')[1]
if '```' in MermaidFlowchart:
    MermaidFlowchart = MermaidFlowchart.split('```')[0]

# Saving Mermaid Flowchart
with open('flowchart.mmd', 'w') as f:
    f.write(MermaidFlowchart)

print('\033[92m' + "Mermaid Flowchart saved in flowchart.mmd ✅\n" + '\033[0m')

# Assuming the Mermaid code is in a file called 'mermaid.mmd'
mermaid_file = BASE_DIR + '/flowchart.mmd'
output_file = BASE_DIR + '/outputs/output.png'

# check if outputs folder exists
if not os.path.exists(BASE_DIR + '/outputs'):
    os.makedirs(BASE_DIR + '/outputs')

# Run the mmdc command
try:
    subprocess.run(['mmdc', '-i', mermaid_file, '-o', output_file, '-b', 'transparent', '-s', '10'])
    print('\033[92m' + "Mermaid Flowchart saved in output.png ✅\n" + '\033[0m')
except Exception as e:
    print('\033[91m' + "Mermaid Flowchart generation failed ❌\n" + '\033[0m')
    print("Exception details:", e)

print('\033[93m' + "------------------------------------------------------------------------------------------------------------------------" + '\033[0m')