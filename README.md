# Resilient Microservices Platform

This project demonstrates a resilient microservices architecture that incorporates key Site Reliability Engineering (SRE) principles such as monitoring, alerting, and chaos engineering.

## Components

- **User Service:** A simple Flask application that exposes a welcome endpoint and Prometheus metrics.
- **Order Service:** Another Flask application similar to the user service.
- **Prometheus:** Collects and scrapes metrics from the microservices.
- **Grafana:** Visualizes the metrics from Prometheus.
- **Chaos Monkey:** A basic script that randomly stops one of the services to simulate failures.
- **CI/CD Pipeline:** Uses GitHub Actions to build, test, and deploy the services with Docker Compose.
