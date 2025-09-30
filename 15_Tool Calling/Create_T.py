from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# print(multiply.invoke({'a':3, 'b':4}))
# print("-"*50)

