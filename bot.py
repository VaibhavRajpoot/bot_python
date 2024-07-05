from openai import OpenAI

client = OpenAI(api_key='sk-proj-UYVtbp0JvCgNapJvyXYrT3BlbkFJcTS5pAa54r93lzzIUwM4')

# Function to interact with the OpenAI GPT-4 model
def chat_with_bot(prompt):
    response = client.completions.create(model="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.7)
    return response.choices[0].text.strip()


def main():
    user_info = {}
    initial_prompt = "You are a friendly assistant. Greet the user and ask how you can help them."

    bot_response = chat_with_bot(initial_prompt)
    print(f"Bot: {bot_response}")
    user_input = input("You: ")


    bot_prompt = f"{user_input}\n\nAsk the user for his/her name"
    bot_response = chat_with_bot(bot_prompt)
    print(f"Bot: {bot_response}")
    user_name = input("You: ")
    user_info["name"] = user_name

    bot_prompt = f"User: {user_name}\n\nThank the user and politely ask the user for the email address"
    bot_response = chat_with_bot(bot_prompt)
    print(f"Bot: {bot_response}")
    user_email = input("You: ")
    user_info["email"] = user_email

    bot_prompt = f"User: {user_email}\n\nNow ask the user in which company does he work?"
    bot_response = chat_with_bot(bot_prompt)
    print(f"Bot: {bot_response}")
    user_company = input("You: ")
    user_info["company"] = user_company

    bot_prompt = f"User: {user_company}\n\nBot: Thank you, {user_name} from {user_company}. I have stored your information."


    # Print the stored information
    print("\nStored User Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
