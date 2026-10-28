# Python Application — DevOps CI/CD Pipeline

## Project Overview

This project demonstrates how to containerize a Python application and automate its testing, security scanning, and deployment using DevOps tools.

The goal is to build a repeatable CI/CD workflow that helps detect issues early and deploy a working application.

## Technology Stack

- **Programming language:** Python
- **Version control:** Git and GitHub
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Security scanning:** Trivy
- **Testing:** Python `unittest`
- **Container registry:** Docker Hub

## Architecture

Developer → GitHub → Jenkins → Automated Tests → Docker Build → Trivy Security Scan → Docker Hub → Deployment → Health Check

The pipeline is configured to automate these stages. Actual execution results may vary depending on the current pipeline configuration and environment.

## Application

The Python application responds with:

```text
Hello! My first DevOps project is running.
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Avinash1707/devops-python-project.git
cd devops-python-project
```

### 2. Run the application

```bash
python app.py
```

Open `http://localhost:8000` in your browser.

## Run Tests

```bash
python -m unittest -v test_app.py
```

## Build and Run with Docker

Build the image:

```bash
docker build -t devops-python-app:latest .
```

Run the container:

```bash
docker run -d --rm --name python-app-test -p 8001:8000 devops-python-app:latest
```

Test the application:

```bash
curl http://localhost:8001
```

Stop the container:

```bash
docker stop python-app-test
```

## Security

Trivy is used to scan the Docker image for known vulnerabilities.

The image has reported unresolved HIGH-severity findings in Debian packages and pip's embedded software bill of materials (SBOM). These findings require further investigation; the image should not be described as vulnerability-free.

## Key Learning Outcomes

- Managing source code with Git and GitHub
- Writing and executing automated Python tests
- Building Docker images
- Running containers with port mapping
- Configuring Jenkins pipeline stages
- Scanning container images with Trivy
- Verifying application health after deployment

## Future Improvements

- Investigate and remediate outstanding security findings.
- Add a `.dockerignore` file.
- Improve automated testing and pipeline failure handling.
- Add monitoring and logging.
- Document deployment and rollback procedures.