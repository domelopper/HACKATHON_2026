from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = "AIzaSyC9qx7WZR-joQPamj1LvrnVpLxnrX02mMU")
MODEL = "gemini-3.1-flash-live-preview" 
PROMPT = "Hola, que es un Hackathon"
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Como es un saque legal en PingPong en pocas palabras"
)
print(response.text)