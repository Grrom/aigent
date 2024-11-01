from flask import Flask, request
from main import send_prompt

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/send_prompt", methods=["POST"])
def prompt():
    return send_prompt(request)


if __name__ == "__main__":
    app.run(debug=True)
