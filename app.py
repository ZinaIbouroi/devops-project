from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import Counter, generate_latest
import os
import datetime
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total requests')

@app.before_request
def count_requests():
    REQUEST_COUNT.inc()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

tasks = []

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

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
    logger.info("Add task request received")
    data = request.get_json(silent=True)

    if not data or "title" not in data:
        logger.warning("Invalid task creation attempt")
        return {"error": "Title is required"}, 400

    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    logger.info(f"Task created with id={task.id}")

    return {"id": task.id, "title": task.title}, 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    logger.info("Fetching tasks from DB")
    tasks = Task.query.all()

    logger.info(f"{len(tasks)} tasks retrieved")

    return [{"id": t.id, "title": t.title} for t in tasks]

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    logger.info(f"Delete request for task id={task_id}")
    
    task = Task.query.get(task_id)

    if not task:
        logger.warning(f"Task not found: id={task_id}")
        return {"error": "Task not found"}, 404

    db.session.delete(task)
    db.session.commit()

    logger.info(f"Task deleted: id={task_id}")

    return {"message": "Task deleted"}

@app.route("/metrics")
def metrics():
    logger.info("Metrics endpoint accessed")
    return generate_latest(), 200, {'Content-Type': 'text/plain'}
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


    
