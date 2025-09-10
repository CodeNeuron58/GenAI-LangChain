# Import required modules from langchain for text splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# Sample Python code as a text string demonstrating a Student class
text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Aarav", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

# Initialize the RecursiveCharacterTextSplitter with Python language settings
# chunk_size: Maximum size of each text chunk (in characters)
# chunk_overlap: Number of characters to overlap between chunks (set to 0 for no overlap)

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

# Split the input text into chunks using the configured splitter
chunks = splitter.split_text(text)

# Print the results
print(len(chunks))  # Display the total number of chunks created
print(chunks[1])    # Display the second chunk of the split text
