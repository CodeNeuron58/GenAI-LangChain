import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_key:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN not found in .env file")

client = InferenceClient(
    provider="novita",
    api_key=api_key
)


completion = client.chat.completions.create(
    model="zai-org/GLM-4.5",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message.content)