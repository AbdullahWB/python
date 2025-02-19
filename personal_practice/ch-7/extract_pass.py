import re

text = "Your OTP is 8965. Use this code to verify your account."
match = re.search(r'\b\d{4}\b', text)  # Find 4-digit number

if match:
    print(f"Extracted Password: {match.group()}")
else:
    print("No 4-digit number found.")
