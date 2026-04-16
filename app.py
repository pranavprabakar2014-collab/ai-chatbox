from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
import os
from openai import OpenAI

client = OpenAI(api_Key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI like ChatGPT."},
            {"role": "user", "content": user_msg}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

app.run(host="0.0.0.0", port=5000)