# DevOps CI/CD Project 🚀 (Docker, CI/CD & Cloud Deployment on Render)

## 🌐 Live Demo
👉https://devops-app-7704.onrender.com

### Healthcheck
👉 https://devops-app-7704.onrender.com/health

---

## 📌 Overview
This project demonstrates a production-like DevOps workflow:
- Flask web application
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Automated API testing with status code validation
- Dependency security scanning using pip-audit
- Environment variable configuration
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
http://localhost:5000

---

## 🩺 Healthcheck
```bash
curl http://localhost:5000/health
```

Expected response:
```
{"status": "ok"}
```

---

## 🔄 CI/CD Pipeline

Triggered on every push to `main`.

### Steps:
- Install dependencies
- Run unit tests (pytest)
- Security scan with pip-audit
- Build Docker image
- Run container
- Test endpoints:
  - `/`
  - `/health`

---

## 🧪 Automated Tests

```bash
PYTHONPATH=. pytest
```

---

## 🔐 Security

The project integrates dependency vulnerability scanning using:

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

Healthcheck:
https://devops-app-7704.onrender.com/health

---

## ⚙️ Environment Variables

| Variable | Description | Default |
|----------|------------|--------|
| APP_MESSAGE | Message displayed on homepage | Hello DevOps 👋 |

---

## 📈 Key Learnings
- Containerizing applications with Docker
- Building CI/CD pipelines with GitHub Actions
- Writing and integrating unit tests (pytest)
- Implementing API healthchecks
- Managing environment variables
- Performing dependency security scanning
- Publishing Docker images to a registry
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
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── main.yml
```

---

## 🔗 Future Improvements
- Add integration tests
- Improve security scanning (SAST/DAST)
- Deploy with Infrastructure as Code (Terraform)
- Add monitoring and logging