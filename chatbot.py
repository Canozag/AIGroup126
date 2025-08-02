from google.genai import Client
import os

def init_client():
    return Client(api_key=os.getenv("GOOGLE_API_KEY"))

def chatbot_response(user_input: str) -> str:
    client = init_client()
    prompt = (
        "You are a supportive chatbot helping people quit smoking. "
        "Always include a disclaimer that you are not a medical professional.\n\n"
        f"User says: {user_input}"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )
    return response.text

def main():
    print("QuitBot: I'm here to support your journey. I'm not a healthcare professional—please consult one.")
    while True:
        msg = input("You: ")
        if msg.lower() in ("exit", "quit"):
            break
        print("Bot:", chatbot_response(msg))

if __name__ == "__main__":
    main()
