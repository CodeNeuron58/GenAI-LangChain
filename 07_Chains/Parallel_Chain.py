from itertools import chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

model_1 = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    model_name = "mistralai/mistral-7b-instruct:free",
    openai_api_key=api_token
)

model_2 = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    # model_name = "mistralai/mistral-7b-instruct:free",
    # model_name = "tngtech/deepseek-r1t2-chimera:free",
    model_name = "deepseek/deepseek-r1-0528:free",

    openai_api_key=api_token
)


prompt_1 = PromptTemplate(
    input_variables=['text'],
    template='Generate short and simple notes from the following text \n {text}'

)

prompt_2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

promt_3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'quiz': prompt_2 | model_2 | parser
})

merge_chain = promt_3 | model_2 | parser

Final_chain = parallel_chain | merge_chain

text = """One of the most useful tools for text processing in computer science has been the
regular expression (often shortened to regex), a language for specifying text searchregular
expression
strings. This practical language is used in every computer language, in text process-
ing tools like the Unix tools grep, and in editors like vim or Emacs. Formally, a
regular expression is an algebraic notation for characterizing a set of strings. Reg-
ular expressions are particularly useful for searching in texts, when we have a pat-
tern to search for and a corpus of texts to search through. A regular expressioncorpus
search function will search through the corpus, returning all texts that match the
pattern. The corpus can be a single document or a collection. For example, the
Unix command-line tool grep takes a regular expression and returns every line of
the input document that matches the expression.
A search can be designed to return every match on a line, if there are more than
one, or just the first match. In the following examples we generally underline the
exact string that matches the regular expression and show only the first match. We’ll
show regular expressions delimited by slashes but note that slashes are not part of
the regular expressions.
Regular expressions come in many variants. We’ll be describing extended regu-
lar expressions; different regular expression parsers may only recognize subsets of
these, or treat some expressions slightly differently. Using an online regular expres-
sion tester is a handy way to test out your expressions and explore these variations"""

result = Final_chain.invoke({'text':text})

print(result)

# # pip install grandalf
Final_chain.get_graph().print_ascii()
