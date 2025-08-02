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
