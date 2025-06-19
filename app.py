from flask import Flask, request, jsonify
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

app = Flask(__name__)

@app.route("/chat", methods=["GET", "POST"])
def chat_api():
    if request.method == "GET":
        return jsonify({"message": "Send a POST request with JSON: { 'message': 'your text' }"}), 400

    if user_input.strip().lower() in ["what is your name?", "who are you?", "what your name"]:
        return jsonify({"reply": "I am TruthLens, your AI assistant."})

    response = chat.send_message(user_input)
    return jsonify({"reply": response.text})

@app.route("/", methods=["GET"])
def home():
    return "TruthLens API is up!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
