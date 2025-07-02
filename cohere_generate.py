import cohere
import os

co = cohere.Client("ehLLrmB6T1PgQsHLtpVfPRQd8vNRTagGHJf0EGqX")  # Replace with your actual API key

# Read user input from a file
with open("user_input.txt", "r") as f:
    user_text = f.read().strip()

# Construct the poster-generation prompt
prompt = f"""
You are a poster layout generator. When given a topic or raw notes, respond with a detailed JSON including layout type, style, and 6 clearly labeled panels with full content (titles + 3–5 bullet points or paragraphs per panel). Each panel should be designed for a real trifold brochure. Use structured sections and return only JSON.

Topic: {user_text}
"""

# Call Cohere API
response = co.generate(
    model="command-r-plus",
    prompt=prompt,
    max_tokens=800,
    temperature=0.6
)

# Output the result
print(response.generations[0].text.strip())
