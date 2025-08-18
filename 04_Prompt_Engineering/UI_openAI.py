import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain.chains import LLMChain

# Load environment variables from .env file (make sure to have OPENAI_API_KEY set)
load_dotenv()

# Initialize the OpenAI model (you can specify additional parameters like temperature)
model = ChatOpenAI()  

# Streamlit UI setup: Title for the web app
st.title("Research Paper Summarizer")

# Subtitle explaining the functionality of the app
st.subheader("Select a research paper to summarize")

# --- UI elements for user input ---

# Dropdown to select the research paper
paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Dropdown to select the explanation style
style_input = st.selectbox(
    "Select Explanation Style", 
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

# Dropdown to select the explanation length
length_input = st.selectbox(
    "Select Explanation Length", 
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# --- Load the prompt template ---

# Load the prompt template (make sure 'template.json' exists and is properly formatted)
template = load_prompt('template.json')

# --- Main execution block ---

# Button to trigger the summarization process
if st.button('Summarize'):
    try:
        # Create the chain by combining the template with the model
        chain = template | model
        
        # Pass parameters as a dictionary; keys must match your prompt template's variables
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        # Check what type of object result is—ensure .content is valid; sometimes it may be ['content']
        st.write(result.content)
        
        # Optional: 
        # To save history of previous runs, use st.session_state
        # if 'history' not in st.session_state:
        #     st.session_state['history'] = []
        # st.session_state['history'].append(result.content)
        
    except Exception as e:
        # Better error feedback (for missing API key, bad prompt, etc.)
        st.error(f"Something went wrong: {str(e)}")

# --- Recommendations for further improvements ---
# 1. To allow users to enter their own API key:
# st.sidebar.text_input("Enter your OpenAI API Key", type="password")
# and overwrite os.environ['OPENAI_API_KEY'] appropriately.

# 2. For agent/chaining/more advanced logic, look into LangChain agents and tools

# 3. If you have multiple prompt templates, enable dynamic selection with another selectbox.
