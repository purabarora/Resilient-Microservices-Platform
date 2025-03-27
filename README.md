# Resilient Microservices Platform

A production-grade SRE demo project showcasing containerized microservices, integrated monitoring, chaos engineering, and CI/CD automation. This project demonstrates best practices in building scalable, resilient, and automated infrastructure that can be deployed either via Docker Compose or Kubernetes.

## Overview

This project includes:
- **Microservices:**  
  - **User Service:** A simple Flask app exposing basic endpoints and Prometheus metrics.
  - **Order Service:** Another Flask application that mirrors the functionality of the User Service.
- **Monitoring & Visualization:**  
  - **Prometheus:** Scrapes metrics from the microservices.
  - **Grafana:** Visualizes Prometheus metrics with customizable dashboards.
- **Chaos Engineering:**  
  - **Chaos Monkey:** A job that simulates failures by deleting a random microservice pod to test resiliency.
- **CI/CD Pipeline:**  
  - **GitHub Actions:** Automated build, test, and deployment pipeline for the project.

## Features

- **Containerization:**  
  Each component is containerized with Docker, making the setup reproducible and portable.
- **Dual Deployment Options:**  
  Deploy with Docker Compose for local development or on Kubernetes for production-like environments.
- **Monitoring & Alerting:**  
  Integrated Prometheus and Grafana enable real-time system monitoring.
- **Chaos Engineering:**  
  Built-in chaos monkey simulates failures to validate the system's resiliency.
- **Automated CI/CD:**  
  GitHub Actions ensures code quality and deployment consistency.

## Prerequisites

- [Docker Desktop](https://www.docker.com/get-started) with Kubernetes enabled (or Minikube/Kind for local Kubernetes)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed and configured
- A Docker Hub account (images are tagged under `purabarora`)

## Setup

### 1. Build, Tag, and Push Docker Images

Make sure you are logged in to Docker Hub:
bash
docker login
Build and push each image:

bash
Copy
## User Service
docker build -t purabarora/user-service:latest ./user-service
docker push purabarora/user-service:latest

## Order Service
docker build -t purabarora/order-service:latest ./order-service
docker push purabarora/order-service:latest

## Chaos Monkey
docker build -t purabarora/chaos-monkey:latest ./chaos-monkey
docker push purabarora/chaos-monkey:latest
2. Running Locally with Docker Compose (Optional)
If you prefer to run the project using Docker Compose, use the provided docker-compose.yml file:

bash
Copy
docker-compose up --build
Access the services at:

User Service: http://localhost:5000

Order Service: http://localhost:5001

Prometheus: http://localhost:9090

Grafana: http://localhost:3000

3. Deploying on Kubernetes
The k8s folder contains all Kubernetes manifests.

Deploy the manifests:

bash
Copy
kubectl apply -f k8s/user-service.yaml
kubectl apply -f k8s/order-service.yaml
kubectl apply -f k8s/prometheus.yaml
kubectl apply -f k8s/grafana.yaml
kubectl apply -f k8s/chaos-monkey.yaml
Accessing Services via Port Forwarding
Use port forwarding to access ClusterIP services locally:

bash
Copy
## User Service
kubectl port-forward service/user-service 5000:5000

## Order Service
kubectl port-forward service/order-service 5001:5001

## Prometheus
kubectl port-forward service/prometheus 9090:9090

## Grafana
kubectl port-forward service/grafana 3000:3000

## CI/CD Pipeline
This repository is integrated with GitHub Actions. The workflow file at .github/workflows/ci-cd.yml handles:

Building Docker images

Running tests (if available)

Deploying the Docker Compose setup to ensure continuous integration
