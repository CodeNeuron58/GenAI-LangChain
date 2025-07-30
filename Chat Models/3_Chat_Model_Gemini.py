from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini‑1.5‑pro",     # or "gemini‑2.0‑flash", etc.
)

# For simple single-message usage:
result = model.invoke("What are the 7 continents?")
print(result.content)

