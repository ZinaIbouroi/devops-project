from flask import Flask, request, jsonify, render_template
import os
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return render_template("ui.html")

@app.route("/health")
def health():
    logger.info("Healthcheck OK")
    return {"status": "ok"}, 200

@app.route("/endpoint_home")
def endpoint_home():
    logger.info("Home endpoint called")
    return {
        "message": "Task Manager API",
        "endpoints": [
            "/tasks",
            "/tasks (POST)",
            "/tasks/<id> (DELETE)",
            "/health"
        ]
    }

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

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True)

    if not data or "title" not in data:
        logger.warning("Invalid task creation attempt")
        return {"error": "Title is required"}, 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"]
    }

    tasks.append(task)
    logger.info(f"Task added: {task}")

    return task, 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    logger.info(f"Fetching tasks: {len(tasks)} tasks")
    return tasks

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    initial_len = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == initial_len:
        logger.warning(f"Task not found: {task_id}")
        return {"error": "Task not found"}, 404

    logger.info(f"Task deleted: {task_id}")
    return {"message": "Task deleted"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
