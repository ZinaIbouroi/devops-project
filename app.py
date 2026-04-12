from flask import Flask, request, jsonify
import os
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/health")
def health():
    logger.info("Healthcheck OK")
    return {"status": "ok"}, 200

@app.route("/")
def hello():
    message = os.getenv("APP_MESSAGE", "Hello DevOps 👋")
    logger.info("Home endpoint called")
    return message

@app.route("/info")
def info():
    logger.info("Info endpoint called")
    return {
        "app": "devops-project",
        "version": "1.0",
        "time": datetime.datetime.utcnow().isoformat()
    }

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)

    if not data:
        logger.warning("No JSON received")
        return {"error": "No JSON received"}, 400

    logger.info(f"Received data: {data}")

    return jsonify({
        "received": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
