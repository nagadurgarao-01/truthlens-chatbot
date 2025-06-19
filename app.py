from flask import Flask, request, jsonify
import google.generativeai as genai
import os

# Load API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the key is actually present
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables!")

# Configure the model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

app = Flask(__name__)

@app.route("/chat", methods=["GET","POST"])
def chat_api():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Missing 'message' in request"}), 400

        user_input = data["message"]

        if user_input.strip().lower() in ["what is your name?", "who are you?", "what your name","What is your name","name","Tell your name","tell about your slef"]:
            return jsonify({"reply": "I am TruthLens, your AI assistant."})

        response = chat.send_message(user_input)
        return jsonify({"reply": response.text})
    
    except Exception as e:
        print(f"Internal Server Error: {e}")
        return jsonify({"error": f"Internal Server Error: {e}"}), 500

@app.route("/", methods=["GET"])
def home():
    return "TruthLens API is up!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
