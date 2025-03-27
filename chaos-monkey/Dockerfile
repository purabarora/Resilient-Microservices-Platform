FROM python:3.9-slim
# Install docker-compose to allow running commands
RUN apt-get update && apt-get install -y docker-compose && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY chaos.py .
CMD ["python", "chaos.py"]
