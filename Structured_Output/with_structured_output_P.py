from langchain_ollama import ChatOllama  # Importing ChatOllama class for interfacing with the language model
from pydantic import BaseModel, Field
from typing import List, Optional, Literal  # Importing necessary types for the model

# Initialize the model with 'llama3.1'
model = ChatOllama(model="llama3.1")
print("result generating...")


# Define the schema for the structured output using Pydantic's BaseModel
# This allows us to specify the exact format we expect the model to return
class Review(BaseModel):
    # List of key themes discussed in the review
    key_themes: List[str] = Field(..., description="Write down all the key themes discussed in the review in a list")
    
    # A brief summary of the review, capturing the main points in a few sentences
    summary: str = Field(..., description="A brief summary of the review")
    
    # Sentiment of the review: can be 'pos', 'neg', or 'neutral'
    sentiment: Literal["pos", "neg", "neutral"] = Field(..., description="Return sentiment of the review either negative, positive or neutral")
    
    # Optional list of pros mentioned in the review (e.g., positive features of the product)
    pros: Optional[List[str]] = Field(None, description="Write down all the pros inside a list")
    
    # Optional list of cons mentioned in the review (e.g., negative features of the product)
    cons: Optional[List[str]] = Field(None, description="Write down all the cons inside a list")
    
    # Optional name of the reviewer if mentioned in the review
    name: Optional[str] = Field(None, description="Write the name of the reviewer")

# Create a structured output model by applying the Review schema to the base model
# This ensures the output from the model matches the structure defined in the Review class
structured_model = model.with_structured_output(Review)

# Invoke the model with a sample review and store the result
result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! 
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. 
The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. 
What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. 
Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. 
Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? 
The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by jit
""")

# Print the structured result returned by the model

print(result.name)  # pyright: ignore[reportAttributeAccessIssue, reportIndexIssue]
