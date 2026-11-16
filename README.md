# DevOps CI/CD Project 🚀 (Task Manager API with UI, Docker & Cloud Deployment)

## 🌐 Live Demo
👉 https://devops-app-7704.onrender.com

### Healthcheck
👉 https://devops-app-7704.onrender.com/health

---

## 📌 Overview
This project demonstrates a production-like DevOps workflow applied to a real application:

- Task Manager API (Flask)
- Web UI for interacting with the API
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Automated API testing with status code validation
- Dependency security scanning using pip-audit
- Environment variable configuration
- Application logging for observability
- Healthcheck endpoint
- Docker image published on Docker Hub
- Deployed on Render (cloud platform)

---

## 🧱 Tech Stack
- Python (Flask)
- Docker
- GitHub Actions
- Gunicorn
- Render (Cloud)
- HTML / JavaScript (UI)

---

## 🚀 Application Features

### 📝 Task Management
- Add tasks
- List tasks
- Delete tasks

### 🌐 Web Interface
- User-friendly UI accessible at `/`
- Dynamic updates (fetch API)
- Table display of tasks
- Delete actions directly from UI

### 📡 API Endpoints

| Method | Endpoint | Description |
|-------|--------|------------|
| GET | `/` | Web UI |
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a task |
| DELETE | `/tasks/<id>` | Delete a task |
| GET | `/health` | Healthcheck |
| GET | `/info` | App metadata |

---

## 🚀 Run locally

### Build Docker image
```bash
docker build -t devops-app .
```

### Run container
```bash
docker run -p 5000:5000 devops-app
```

### With environment variable
```bash
docker run -p 5000:5000 -e APP_MESSAGE="Hello from Docker 🚀" devops-app
```

### Access the app
👉 http://localhost:5000

---

## 🧪 Automated Tests

Run tests locally:

```bash
PYTHONPATH=. pytest
```

---

## 🔄 CI/CD Pipeline

Triggered on every push to `main`.

### Pipeline steps:
- Install dependencies
- Run unit tests (pytest)
- Security scan (pip-audit)
- Build Docker image
- Run container
- Test API endpoints (`/`, `/health`, `/tasks`)

---

## 🔐 Security

Dependency vulnerability scanning is implemented using:

```bash
pip-audit
```

Note: Vulnerabilities are detected but do not block the pipeline in this context.

---

## 🐳 Docker Hub

Image available here:

👉 https://hub.docker.com/r/izh0407/devops-app

Run directly:

```bash
docker run -p 5000:5000 izh0407/devops-app:latest
```

---

## ☁️ Cloud Deployment (Render)

The application is deployed using:

- Platform: Render
- Runtime: Python
- Web server: Gunicorn

The service is automatically deployed from the GitHub repository.

👉 Live URL:
https://devops-app-7704.onrender.com

---

## ⚙️ Environment Variables

| Variable | Description | Default |
|----------|------------|--------|
| APP_MESSAGE | Application message | Hello DevOps 👋 |

---

## 📈 Key Learnings
- Building REST APIs with Flask
- Designing a simple fullstack application (API + UI)
- Containerizing applications with Docker
- Implementing CI/CD pipelines with GitHub Actions
- Writing unit tests with pytest
- Integrating security scanning (pip-audit)
- Managing environment variables
- Implementing application logging
- Deploying applications to the cloud (Render)

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── .dockerignore
├── templates/
│   └── ui.html
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── main.yml
```

---

## 🔗 Future Improvements
- Add database (PostgreSQL)
- Add authentication (JWT)
- Improve UI/UX
- Add monitoring and metrics
- Infrastructure as Code (Terraform)