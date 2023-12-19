from langchain.chat_models import ChatOpenAI, ChatCohere
from langchain.schema import SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
# llm = ChatCohere(temperature=0.3)

class Chains:
    def __init__(self, *args):
        self._chains = args

    def chain(self, PromptTemplate, parser = None):
        message = [
            SystemMessage(content = PromptTemplate)
        ]
        output = llm(message)
        if parser is None:
            return output.content
        else:
            return parser.parse(output.content)
    