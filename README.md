# DevOps CI/CD Project 🚀

## 📌 Overview
This project demonstrates a production-like DevOps workflow:
- Flask web application
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Automated API testing
- Environment variable configuration
- Healthcheck endpoint
- Docker image published on Docker Hub

---

## 🧱 Tech Stack
- Python (Flask)
- Docker
- GitHub Actions

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
- Build Docker image
- Run container
- Test endpoints:
  - `/`
  - `/health`

---

## 🧪 Automated Tests

```bash
curl http://localhost:5000
curl http://localhost:5000/health
```

---

## 🐳 Docker Hub

Image available here:

👉 https://hub.docker.com/r/izh0407/devops-app

Run directly:

```bash
docker run -p 5000:5000 izh0407/devops-app:latest
```

---

## 📈 Key Learnings
- Containerizing applications with Docker
- Building CI/CD pipelines with GitHub Actions
- Using environment variables for configuration
- Implementing healthcheck endpoints
- Publishing Docker images to a registry

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/main.yml
```

---

## 🔗 Future Improvements
- Add unit tests
- Deploy to cloud (AWS / Azure)
- Use infrastructure as code (Terraform)