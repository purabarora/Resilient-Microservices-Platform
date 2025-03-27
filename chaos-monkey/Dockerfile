# Use a minimal Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy chaos.py to container
COPY chaos.py .

# Install Kubernetes client
RUN pip install kubernetes

# Run chaos.py
CMD ["python", "chaos.py"]
