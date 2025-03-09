from flask import Flask, request, render_template
import requests

app = Flask(__name__)

GEMINI_API_KEY = ""
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText?key={GEMINI_API_KEY}"

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    
    if request.method == "POST":
        user_prompt = request.form.get("prompt")

        if user_prompt:
            payload = {
                "prompt": {"text": user_prompt}
            }
            
            try:
                response = requests.post(GEMINI_API_URL, json=payload)
                data = response.json()
                response_text = data.get("candidates", [{}])[0].get("output", "No response from AI.")
            except Exception as e:
                response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
