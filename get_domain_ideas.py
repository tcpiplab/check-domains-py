import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Read the input words from domains.txt
with open('domains.txt', 'r') as f:
    input_words = f.read().split()

# Construct the prompt
prompt = (
    f"Generate 20 domain name ideas related to the following words: {', '.join(input_words)}.\n"
    "The domain names should be single words or pairs of words without any spaces.\n"
    "If a domain name is formed by combining two words, please also output the same pair of words joined by a single '-' character on the next line.\n"
    "Do not include the top-level domain.\n"
    "Only generate 20 domain name ideas in total."
)

# Make the API call
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates domain name ideas."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500,
    n=1,
    temperature=0.7,
)

# Extract and print the response
domain_ideas = response['choices'][0]['message']['content']
print(domain_ideas)