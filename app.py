from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Phishing keywords
PHISHING_KEYWORDS = [
    "verify", "login", "urgent", "click", "prize",
    "refund", "blocked", "suspended", "reset", "confirm", "win"
]

def detect_phishing(text):
    text = text.lower()

    # Keyword check
    for word in PHISHING_KEYWORDS:
        if word in text:
            return "🚨 PHISHING DETECTED"

    # Suspicious link pattern
    if re.search(r"http[s]?://.*(verify|secure|login|update)", text):
        return "🚨 PHISHING DETECTED"

    return "✅ SAFE MESSAGE"


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_text = request.form["text"]
        result = detect_phishing(user_text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
