from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env (make sure you have OPENAI_API_KEY set)
load_dotenv()

# Initialize model with Llama
model = ChatOllama(model="llama3.1")

# Input prompt for the paper
print("Select Research Paper Name:")
paper_input = input("""
    1. Attention Is All You Need
    2. BERT: Pre-training of Deep Bidirectional Transformers
    3. GPT-3: Language Models are Few-Shot Learners
    4. Diffusion Models Beat GANs on Image Synthesis
    \nEnter the number of the paper you want to summarize: """)
papers = [
    "Attention Is All You Need", 
    "BERT: Pre-training of Deep Bidirectional Transformers", 
    "GPT-3: Language Models are Few-Shot Learners", 
    "Diffusion Models Beat GANs on Image Synthesis"
]
paper_input = papers[int(paper_input) - 1]

# Input prompt for the style
print("\nSelect Explanation Style:")
style_input = input("""
    1. Beginner-Friendly
    2. Technical
    3. Code-Oriented
    4. Mathematical
    \nEnter the number of the explanation style: """)
styles = [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical"
]
style_input = styles[int(style_input) - 1]

# Input prompt for the length of the explanation
print("\nSelect Explanation Length:")
length_input = input("""
    1. Short (1-2 paragraphs)
    2. Medium (3-5 paragraphs)
    3. Long (detailed explanation)
    \nEnter the number of the length: """)
lengths = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
]
length_input = lengths[int(length_input) - 1]

# Load the prompt template
template = PromptTemplate.from_template("""
    You are a research assistant. Summarize the following paper in the style of {style_input} with the length of {length_input}.
    Paper: {paper_input}
""")

# Create the chain with the model
chain = template | model

# Execute the chain when the user confirms
print("\nGenerating summary...")

try:
    # Run the chain with user input
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })

    # Display the result
    print("\nSummary:\n")
    print(result.content)
    
except Exception as e:
    print(f"Something went wrong: {str(e)}")