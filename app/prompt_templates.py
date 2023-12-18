from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

#packages
from packages.prompts import *

class GetPromptTemplates:
  def __init__(self, topic):
    self.topic = topic
    self.question_parser = CommaSeparatedListOutputParser()
  
  def ResearchPromptTemplate(self, questions = ''):
    if questions != '':
      research_bot_prompt = research_bot_prompt_1 + "\n\nQuestions Answered by the user : " + questions + "\n\n" + research_bot_prompt_2;
    else:
      research_bot_prompt = research_bot_prompt_1 + "\n\n" + research_bot_prompt_2;
    
    ResearchPromptTemplate = PromptTemplate(template= research_bot_prompt, input_variables=["Topic"])
    # partial_variables={"format_instructions": self.research_parser.get_format_instructions()} 
    return ResearchPromptTemplate.format_prompt(Topic = self.topic).to_string()
  
  def QuestionPromptTemplate(self):
    QuestionPromptTemplate = PromptTemplate(template= question_forming_prompt, input_variables=["Topic"], partial_variables={"format_instructions": self.question_parser.get_format_instructions()})

    return QuestionPromptTemplate.format_prompt(Topic = self.topic).to_string()
  
  def MermaidPromptTemplate(self, information):
    MermaidPromptTemplate = PromptTemplate(template= mermaid_maker_prompt, input_variables=["information"])

    return MermaidPromptTemplate.format_prompt(information = information).to_string()