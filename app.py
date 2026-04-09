from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/")
def hello():
    message = os.getenv("APP_MESSAGE", "Hello DevOps 👋")
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
