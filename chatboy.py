import random
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get-response", methods=["POST"])
def get_bot_response():
    user_text = request.form["message"]
    bot_response = get_response(user_text)
    return str(bot_response)

def get_response(user_text):
    # Load the chatbot's data
    with open("chatbot_data.json", "r") as f:
        data = json.load(f)

    # Find the best match for the user's message
    best_match = ""
    best_score = 0
    for pattern, responses in data["patterns"].items():
        for pattern_text in pattern.split("|"):
            score = similarity(user_text, pattern_text)
            if score > best_score:
                best_match = random.choice(responses)
                best_score = score

    return best_match

def similarity(s1, s2):
    # Calculate the similarity between two strings
    s1 = set(s1.lower().split())
    s2 = set(s2.lower().split())
    return len(s1 & s2) / len(s1 | s2)

if __name__ == "__main__":
    app.run(debug=True)
