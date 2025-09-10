# CharacterTextSplitter

# Import necessary libraries from langchain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load the PDF document
loader = PyPDFLoader('10_Text Splitters/dl-curriculum.pdf')  # Change the file path if necessary

# Load the document into a list of pages (each page is a Document object)
docs = loader.load()

# Initialize the CharacterTextSplitter
splitter = CharacterTextSplitter(
    chunk_size=200,  # Maximum number of characters per chunk
    chunk_overlap=0,  # No overlap between chunks
    separator=''  # No separator between chunks (can be customized)
)

# Split the document into chunks based on the specified parameters
result = splitter.split_documents(docs)

# Print the content of the second chunk (index 1)
print(result[1].page_content)
