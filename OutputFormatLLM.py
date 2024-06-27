import openai
import json

# Replace with your OpenAI API key
api_key = 'your_openai_api_key_here'

# Set the OpenAI API key
openai.api_key = api_key

def generate_response(prompt):
    try:
        # Generate response using LLM-213b-chatgptq model
        response = openai.Completion.create(
            engine="text-llm-213b-chatgptq",  # Use LLM-213b-chatgptq engine
            prompt=prompt,
            max_tokens=150  # Adjust max_tokens based on desired response length
        )

        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

# Define the prompt for the transformation task
prompt = """
Describe a transformation task involving data attributes and their aggregation.
For example:
Input attributes:
- Age: integer, Age of loan applicants
- Balance: decimal, Loan balance
- Country: string, Country of loan applicants

Output attributes:
- Country: string, Country grouped by in the output
- sum(balance): decimal, Sum of balance for loans grouped by country

Transformation:
SQL transformation to compute sum of balances for loans grouped by country where age of loan applicants is greater than 19.
"""

# Generate response based on the prompt
response_text = generate_response(prompt)

if response_text:
    # Parse the response text into a Python dictionary
    response_dict = json.loads(response_text)

    # Print the formatted JSON response
    print(json.dumps(response_dict, indent=2))

else:
    print("Failed to generate a response.")
