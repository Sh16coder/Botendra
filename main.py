import google.generativeai as genai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

genai.configure(api_key=os.getenv("AIzaSyBD3ypw-O-9HnXI941GP-hvMI880Cmhryw"))

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question")

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_question)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
