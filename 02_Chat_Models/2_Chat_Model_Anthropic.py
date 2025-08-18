from langchain_anthropic import ChatAnthropic
"""
This script demonstrates how to use the `langchain_anthropic` library to interact with Anthropic's Claude v3 (Opus) language model.
It loads the Anthropic API key from a `.env` file using `dotenv`, initializes the `ChatAnthropic` agent, and sends a sample prompt.
The script prints both the full response object and the generated answer content.
Steps:
1. Load environment variables (e.g., ANTHROPIC_API_KEY) from a `.env` file.
2. Initialize the `ChatAnthropic` model with the desired Claude v3 variant.
3. Optionally, configure parameters such as temperature.
4. Send a prompt to the model and receive a response.
5. Print the response object and the answer content.
"""
from dotenv import load_dotenv
import os

# Load environment variables from .env (e.g., ANTHROPIC_API_KEY)
load_dotenv()

# Initialize the ChatAnthropic agent using Claude v3 (Sonnet)
# You MUST have ANTHROPIC_API_KEY set in your .env file, not OPENAI_API_KEY
# Example: ANTHROPIC_API_KEY=your_claude_api_key

model = ChatAnthropic(model_name='claude-3-opus-20240229', timeout=60, stop=None)


# timeout=60

#     Sets how long the client library will wait for a response before throwing a timeout error.

#     Default is typically 10 minutes, but here it's configured to 60 seconds
#     Reddit+5npm+5GitHub+5
#     .

#     If the request fails due to timeout, it will be retried automatically (Anthropic retries by default up to two times) unless you configure maxRetries differently
#     npm
#     .

# stop=None

#     stop (or stop_sequences) gives a list of tokens or substrings at which generation should be halted.

#     If None, the model will stop according to its own logic—typically at end_turn, when it believes it's finished—unless it hits max_tokens limit or a custom sequence is specified
#     LangChain Python API+1LangChain+1
#     LangChain+9Anthropic
# You can set temperature if desired, e.g.,
# models = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.1)



# Invoke the model with a user prompt.
result = model.invoke("What are the 7 continents?")

# Print the full response object
print(result)

# Print just the answer string
print(result.content)
