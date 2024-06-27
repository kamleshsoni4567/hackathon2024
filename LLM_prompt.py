import openai

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

# Example prompt template
prompt_template = "As an AI language model, I can assist you with various queries. Please provide a prompt:"

# Get user input or specify your own prompt
user_prompt = input(f"{prompt_template}\n")

# Generate response based on user input
if user_prompt.strip():
    response = generate_response(user_prompt)
    if response:
        print("LLM-213b-chatgptq's response:")
        print(response)
    else:
        print("Failed to generate a response.")
else:
    print("Please provide a prompt.")
