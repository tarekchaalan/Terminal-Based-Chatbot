import openai
import os

# Load your API key from an environment variable
# (not recommended) or paste it here directly if you don't want to use env vars.
# To set an environment variable on Mac/Linux, run the following command in the Terminal:
# export OPENAI_API_KEY=API_HERE
# no need to use quotes around the API key
# On Windows, run this command in the CMD:
# set OPENAI_API_KEY=API_HERE

client = openai.Client()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    messages = [{"role": "system", "content": ""}]

    while True:
        message = input("👤: ")
        if message.lower() == "quit":
            print("🤖: Bye!\n")
            break

        messages.append({"role": "user", "content": message})
        content = client.chat.completions.create(
            model="gpt-3.5-turbo", #modify this to change the model
            messages=messages
        )

        chat_message = content.choices[0].message
        print(f"🤖: {chat_message.content}")
        messages.append({"role": "assistant", "content": chat_message.content})

if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!\n")
    chatbot()
