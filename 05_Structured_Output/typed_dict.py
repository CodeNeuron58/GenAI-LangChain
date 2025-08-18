# experiment

from typing import TypedDict

class person(TypedDict):
    name: str
    age: int
    email: str
    
person_1: person = {"name": "jit", "age": 19, "email": "jit@gmail.com"}
print(person_1)

