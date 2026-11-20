# AWS ECS Fargate Production Deployment

## Project Overview

A Flask REST API deployed using Docker,
Amazon ECR and Amazon ECS Fargate.

## Technologies

- Python
- Flask
- Docker
- AWS ECR
- AWS ECS Fargate
- Application Load Balancer
- CloudWatch

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Application information |
| GET | /health | Health check |
| GET | /version | Application version |

## Docker

Build:

    docker build -t flask-api:v1 .

Run:

    docker run -d -p 5000:5000 flask-api:v1

Test:

    curl http://localhost:5000/health