import openai
import time

openai.api_key = "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"

def query_openai_with_retry(input_text):
    attempts = 0
    while attempts < 5:
        try:
            # Make the request to OpenAI
            response = openai.Completion.create(
                model="gpt-4o",  # Use a valid model
                prompt=input_text,
                max_tokens=100
            )
            return response  # Return the response only if successful
        except openai.error.RateLimitError:
            attempts += 1
            print("Rate limit exceeded, retrying in 5 seconds...")
            time.sleep(5)  # Wait before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return None  # Return None if all retries fail

# Example usage
input_text = "Explain recursion in Python."
response = query_openai_with_retry(input_text)

# Ensure that the response is valid and contains the expected structure
if response and 'choices' in response and len(response['choices']) > 0:
    print(response['choices'][0]['text'].strip())  # Correctly access the response
else:
    print("No valid response received.")
