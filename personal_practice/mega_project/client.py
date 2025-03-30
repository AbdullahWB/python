# import openai

# # optional; defaults to `os.environ['OPENAI_API_KEY']`
# openai.api_key = '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'

# # all client options can be configured just like the `OpenAI` instantiation counterpart
# openai.base_url = "https://..."
# openai.default_headers = {"x-foo": "true"}

# completion = openai.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I output all files in a directory using Python?",
#         },
#     ],
# )
# print(completion.choices[0].message.content)
import openai
# import os
# from dotenv import load_dotenv

# # Load API key from .env file
# load_dotenv()
openai.api_key = "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"

# Generate a response from OpenAI
output = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "How do I output all files in a directory using Python?"},
    ],
    # max_tokens=50  # Reduce token limit
)
print(output)
# # Ask OpenAI a question
# response = openai.Completion.create(
#     model="text-davinci-003",  # Or gpt-3.5-turbo or other models
#     prompt="What is recursion in programming?",
#     max_tokens=100  # Limit the response length
# )

# # Print the response
# print(response.choices[0].text.strip())
