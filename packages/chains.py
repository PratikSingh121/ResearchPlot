from langchain.chat_models import ChatOpenAI, ChatCohere
from langchain.schema import SystemMessage
from dotenv import load_dotenv

if load_dotenv() == False:
    print('\033[91m' + "🚫 .env file not found 🚫" + '\033[0m')
    api_key = input("Enter your OpenAI API key and press enter to continue > ")
    with open('.env', 'w') as f:
        f.write(f"OPENAI_API_KEY='{api_key}'")
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
    