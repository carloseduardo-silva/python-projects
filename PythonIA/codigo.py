from dotenv import load_dotenv
import os

from langchain_core.messages import SystemMessage, HumanMessage

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

# resgatar token da API armazenado nas variaveis de ambiente
# load_dotenv()
# chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Estou aprendendo a manipular Inteligencia Artificial utilizando programação")
]

#template de mensagens pergunta e resposta entre usuário e máquina
templateMensagens = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{traduzirTexto}"),
])

#modelo de IA utilizado
modelo = ChatOpenAI(model="gpt-4o-mini")

# interpretador da reposta cheia de info para apenas o texto
parser = StrOutputParser()

#cadeia que permite a execução das funções em cadeia
chain = templateMensagens | modelo | parser

texto = chain.invoke({"idioma": "espanhol", "traduzirTexto": "Ola meu nome é carlos eduardo"})


#utilizar o modelo criado
# resposta = modelo.invoke(mensagens)
#resposta tratada
# texto = parser.invoke(resposta)



print(texto)