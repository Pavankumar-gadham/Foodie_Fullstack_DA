🍽️ Recipe Manager – Full Stack Web Application

A full-stack Recipe Management web application built using Django REST Framework and Angular, with a strong focus on cloud deployment, containerization, and CI/CD automation.
The application allows users to create, manage, and view recipes through a secure and scalable architecture.

🚀 Features

User authentication and authorization

Create, read, update, and delete (CRUD) recipes

RESTful APIs for frontend-backend communication

Responsive Angular frontend

Secure backend with Django REST Framework

Production-ready deployment with Docker and Nginx

Automated CI/CD pipeline using Jenkins

🛠️ Tech Stack
Frontend

Angular

Hosted on AWS S3 (Static Website Hosting)

Backend

Django & Django REST Framework

REST APIs

Database

MySQL

DevOps & Cloud

AWS EC2 (Backend hosting)

AWS S3 (Frontend hosting)

Docker (Containerization)

Jenkins (CI/CD automation)

Nginx (Reverse Proxy)

Linux (Ubuntu)

Git (Version Control)

🏗️ Architecture Overview

Angular frontend is built and deployed to AWS S3 as a static website

Django REST backend runs in a Docker container on AWS EC2

Nginx acts as a reverse proxy for routing API requests

MySQL is used as the backend database

Jenkins CI/CD pipeline automates build and deployment workflows

🔄 CI/CD Pipeline (Jenkins)

Code changes pushed to GitHub trigger Jenkins pipeline

Pipeline stages:

Code checkout from GitHub

Build Docker images

Run basic validation checks

Deploy containers to AWS EC2

Enables faster, repeatable, and reliable deployments

🐳 Dockerized Setup

Separate Docker containers for:

Backend (Django REST API)

Database (MySQL)

Ensures consistent environments across development and production

📂 Project Structure (High Level)
recipe-manager/
├── backend/        # Django REST Framework backend
├── frontend/       # Angular frontend
├── docker/         # Docker configuration files
├── nginx/          # Nginx reverse proxy config
├── Jenkinsfile     # CI/CD pipeline definition
└── README.md

🔐 Security & Best Practices

Environment variables used for sensitive configurations

IAM roles and security groups configured on AWS

Production-ready Nginx reverse proxy setup

Git-based version control and branch management

📈 Key Learnings

End-to-end deployment of a full-stack application on AWS

Hands-on experience with Docker and CI/CD pipelines

Practical exposure to Linux server management and Nginx

Understanding of scalable and maintainable cloud architecture

📌 Future Improvements

Add monitoring and logging (CloudWatch / Prometheus)

Implement HTTPS using SSL certificates

Introduce container orchestration (ECS / Kubernetes)

Add automated testing to CI/CD pipeline

🤝 Contributing

Contributions, suggestions, and improvements are welcome.
Please fork the repository and submit a pull request.

📬 Contact

If you have any questions or feedback, feel free to connect with me on LinkedIn or GitHub.
