import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate a response from OpenAI
output = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "How do I output all files in a directory using Python?"},
    ],
    # max_tokens=50  # Reduce token limit
)
print(output)