import streamlit as st
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from the .env file (this ensures that API keys or other sensitive data are loaded correctly)
load_dotenv()

# Initialize the Llama model for generating summaries
model = ChatOllama(model="llama3.1")

# Streamlit UI setup: Title for the web app
st.title("Research Paper Summarizer")

# Subtitle explaining the functionality of the app
st.subheader("Select a research paper to summarize")

# Create a dropdown for users to select a research paper
papers = [
    "Attention Is All You Need", 
    "BERT: Pre-training of Deep Bidirectional Transformers", 
    "GPT-3: Language Models are Few-Shot Learners", 
    "Diffusion Models Beat GANs on Image Synthesis"
]
# User selects one paper from the list
paper_input = st.selectbox("Select the research paper:", papers)

# Subheader for style selection
st.subheader("\nSelect Explanation Style:")

# Options for different explanation styles
styles = [
    "Beginner-Friendly",
    "Technical",
    "Code-Oriented",
    "Mathematical"
]
# User selects the explanation style from the dropdown
style_input = st.selectbox("Choose an explanation style:", styles)

# Subheader for length selection
st.subheader("\nSelect Explanation Length:")

# Options for the length of the explanation
lengths = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)"
]
# User selects the explanation length from the dropdown
length_input = st.selectbox("Choose the length of the explanation:", lengths)

# Load the prompt template using the selected user inputs
template = PromptTemplate.from_template("""
    You are a research assistant. Summarize the following paper in the style of {style_input} with the length of {length_input}.
    Paper: {paper_input}
""")

# Combine the template with the model to create a chain that generates the summary
chain = template | model

# Action for the user to click the button to generate the summary
if st.button("Generate Summary"):
    # Inform the user that the summary generation is in progress
    st.text("Generating summary...")
    
    try:
        # Run the chain with user input and generate the summary
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        
        # Display the result (the generated summary)
        st.subheader("Summary:")
        st.write(result.content)

    except Exception as e:
        # Handle any errors that might occur and display an error message to the user
        st.error(f"Something went wrong: {str(e)}")
