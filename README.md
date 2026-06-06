# 🛡️ TruthLens Chatbot

TruthLens is an AI-powered chatbot built using Flask and Google's Gemini API. It provides intelligent conversational responses and serves as the backend API for the TruthLens project.

## 🚀 Features

- AI-powered chatbot using Gemini 2.0 Flash
- REST API built with Flask
- Environment variable-based API key security
- Custom identity responses
- JSON-based request and response handling
- Ready for deployment on Render

---

## 📁 Project Structure

```
TRUTHLENS-CHATBOT/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment configuration
└── README.md           # Project documentation
```

---

## ⚙️ Requirements

- Python 3.10+
- Google Gemini API Key
- Flask

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/TRUTHLENS-CHATBOT.git
cd TRUTHLENS-CHATBOT
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file or set environment variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Windows

```bash
set GEMINI_API_KEY=your_api_key
```

### Linux/Mac

```bash
export GEMINI_API_KEY=your_api_key
```

---

## ▶️ Running the Application

```bash
python app.py
```

Server will start at:

```text
http://localhost:5000
```

---

## 📡 API Endpoints

### Home Endpoint

**GET /**

Returns server status.

#### Response

```text
TruthLens API is up!
```

---

### Chat Endpoint

**POST /chat**

Send a message to the chatbot.

#### Request

```json
{
    "message": "Hello"
}
```

#### Response

```json
{
    "reply": "Hello! How can I assist you today?"
}
```

---

## 🧠 Custom Responses

The chatbot responds with a predefined answer for the following queries:

- What is your name?
- Who are you?
- Tell your name
- Name
- Tell about yourself

Example:

```json
{
    "reply": "I am TruthLens, your AI assistant."
}
```

---

## 🛠️ Technologies Used

- Flask
- Google Gemini API
- Python
- Render

---

## ☁️ Deployment on Render

### 1. Push Code to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Create a New Web Service on Render

1. Login to Render
2. Click **New +**
3. Select **Web Service**
4. Connect your GitHub repository
5. Add Environment Variable:

```text
GEMINI_API_KEY = your_api_key
```

6. Deploy

---

## 📄 Example cURL Request

```bash
curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d "{\"message\":\"Hello\"}"
```

---

## 🔒 Security Notes

- Never commit your Gemini API key to GitHub.
- Always use environment variables.
- Add `.env` to `.gitignore`.

Example `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**KOTHEM NAGA DURGARAO**

TruthLens – AI-Powered Fake News Detection & Intelligent Assistance Platform.