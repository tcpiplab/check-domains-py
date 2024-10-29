import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Read the input words from seed_words.txt
with open('seed_words.txt', 'r') as f:
    input_words = f.read().split()

# Construct the prompt
prompt = (
    f"Generate 20 domain name ideas related to the following words: {', '.join(input_words)}.\n"
    "The domain names should be single words or pairs of words without any spaces.\n"
    "If a domain name is formed by combining two words, please also output the same pair of words joined by a single '-' character on the next line.\n"
    "Do not include the top-level domain.\n"
    "Do not include any numbers, bullets, or other characters before the domain names.\n"
    "Only generate 20 domain name ideas in total."
)

# Make the API call
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates domain name ideas."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500,
    n=1,
    temperature=0.7
)

# Extract the response
raw_domain_ideas = response.choices[0].message.content

#print(raw_domain_ideas)

# Process the domain ideas
domain_ideas = []
for line in raw_domain_ideas.split('\n'):
    # Remove any leading/trailing whitespace and skip empty lines
    line = line.strip()
    # Skip lines that start with a number or a hyphen
    if line and not line.startswith('-'): # and not line[0].isdigit():
        # Remove leading digits, dot, and whitespace
        line = re.sub(r'^\d+\.\s*', '', line)
        domain_ideas.append(line)

# Join the processed domain ideas with newlines
suggested_domains = '\n'.join(domain_ideas)

# Print the result
print(suggested_domains)

# TODO call the check_domain_availability.py script with the final domain ideas as input

# TODO write the available domains to a file and to STDOUT
# Write suggested_domains to a file
with open('suggested_domains.txt', 'w') as f:
    f.write(suggested_domains)

