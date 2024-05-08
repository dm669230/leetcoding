import openai
# Set up your OpenAI API key
openai.api_key = ''

# Function to send prompt to OpenAI and get response
def ask_gpt(prompt):
    response = openai.Completion.create(
      engine="text-davinci",  # Use an available model, like "text-davinci"
      prompt=prompt,
      max_tokens=150  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = ask_gpt(user_input)
    print("ChatGPT:", response)

