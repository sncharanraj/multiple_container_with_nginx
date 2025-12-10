---

# Multi-Service DevOps Project

This project demonstrates a multi-service application deployed using **Docker**, **NGINX reverse proxy**, **GitHub Actions**, and an **Azure VM**.
Each push to the `main` branch automatically builds, pushes, and deploys all microservices.

---

## 🚀 Features

* Multi-service architecture (FastAPI + Flask + NGINX)
* Dockerized services with shared networking
* GitHub Actions CI/CD pipeline
* Deployment to Azure VM using SSH automation
* Reverse proxy routing using NGINX
* Endpoints exposed through a single public IP

---

## 🧩 Architecture Diagram

```
                   +------------------------+
                   |     GitHub Repo        |
                   |  (source + workflow)   |
                   +-----------+------------+
                               |
                               | Push triggers CI
                               v
                +-------------------------------+
                |      GitHub Actions CI/CD     |
                |  Build → Push → Deploy        |
                +-------------------------------+
                               |
                               | SSH deploy
                               v
        +------------------------------------------------+
        |                Azure VM                         |
        |------------------------------------------------|
        |  Docker Engine                                 |
        |                                                |
        |  +----------------+     +------------------+    |
        |  |  Service A     |     |   Service B      |    |
        |  | (FastAPI:8001) |     | (Flask:5000)     |    |
        |  +----------------+     +------------------+    |
        |                \             /                  |
        |                 \           /                   |
        |                 +------------------+            |
        |                 |     NGINX Proxy  |            |
        |                 |  Routes: /api1   |------------> Public :9000/api1
        |                 |          /api2   |------------> Public :9000/api2
        |                 +------------------+            |
        +------------------------------------------------+
```

---

## 📁 Project Structure

```
.
├── service-a/          # FastAPI service (API 1)
├── service-b/          # Flask service (API 2)
├── nginx/              # Reverse proxy config
├── docker-compose.yml  # Multi-service definition
└── .github/workflows/
    └── deploy.yml      # CI/CD pipeline
```

---

## 🔧 Tech Stack

* FastAPI, Flask
* Docker, Docker Compose
* NGINX
* GitHub Actions
* Azure Virtual Machine
* GHCR (GitHub Container Registry)

---

## ⚙️ CI/CD Summary

### **CI Stage**

* Builds Docker images for all services
* Pushes latest images to GHCR

### **CD Stage**

* SSH into Azure VM
* Pulls latest Docker images
* Restarts services using Docker Compose

---

## 🌍 Public Endpoints

```
http://<VM_PUBLIC_IP>:9000/api1
http://<VM_PUBLIC_IP>:9000/api2
```

---
