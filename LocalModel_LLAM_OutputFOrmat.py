
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import json

# Path to the downloaded model files
model_path = 'path_to_downloaded_model_directory'  # Replace with your actual path

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

def generate_response(prompt):
    try:
        # Tokenize the prompt and generate response using the model
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs.input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)

        return tokenizer.decode(outputs[0], skip_special_tokens=True)

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
    # Construct the formatted JSON response
    response_dict = {
        "inputAttributes": [
            {"name": "age", "type": "integer", "description": "Age of loan applicants"},
            {"name": "balance", "type": "decimal", "description": "Loan balance"},
            {"name": "country", "type": "string", "description": "Country of loan applicants"}
        ],
        "outputAttributes": [
            {"name": "country", "type": "string", "description": "Country grouped by in the output"},
            {"name": "sum(balance)", "type": "decimal", "description": "Sum of balance for loans grouped by country"}
        ],
        "transformation": {
            "sql": "SELECT country, SUM(balance) FROM Loan WHERE age > 19 GROUP BY country",
            "description": "SQL transformation to compute sum of balances for loans grouped by country where age of loan applicants is greater than 19"
        },
        "response": {
            "text": response_text.strip(),
            "generated_by": "LLM-213b-chatgptq"
        }
    }

    # Print the formatted JSON response
    print(json.dumps(response_dict, indent=2))

else:
    print("Failed to generate a response.")
