# DevOps CI/CD Project 🚀

## 📌 Overview
This project demonstrates a simple DevOps pipeline:
- A Flask web application
- Containerization with Docker
- CI/CD pipeline using GitHub Actions
- Automated API testing

---

## 🧱 Tech Stack
- Python (Flask)
- Docker
- GitHub Actions

---

## 🚀 Run locally

### 1. Build Docker image
```bash
docker build -t devops-app .
```

### 2. Run container
```bash
docker run -p 5000:5000 devops-app
```

### 3. Access the app
Open in your browser:  
http://localhost:5000

---

## 🔄 CI/CD Pipeline

The pipeline is triggered on every push to the main branch.

### Steps:
- Build Docker image
- Run container
- Wait for application startup
- Test API using curl

---

## 🧪 Automated Test

The pipeline verifies the application by sending a request:

```bash
curl http://localhost:5000
```

Expected response:
```
Hello DevOps 👋
```

---

## 📈 Key Learnings
- Containerizing an application with Docker
- Setting up a CI/CD pipeline using GitHub Actions
- Automating application testing
- Understanding deployment workflow basics

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
- Push Docker image to Docker Hub
- Deploy to a cloud provider (AWS / Azure)
- Add unit tests
