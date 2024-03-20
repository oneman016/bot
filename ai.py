import openai

# Set your OpenAI API key
openai.api_key = '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'

def generate_response(prompt):
    try:
        # Use OpenAI's GPT-3 to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50
        ).choices[0].text.strip()
        return response
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    user_prompt = input("Enter your message: ")
    response = generate_response(user_prompt)
    print("Bot's response:", response)
