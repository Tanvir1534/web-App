from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = 'your-openai-api-key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI business assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
