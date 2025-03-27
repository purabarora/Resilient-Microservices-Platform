from flask import Flask, jsonify
from prometheus_client import generate_latest, Counter

app = Flask(__name__)

# Define a Prometheus counter for tracking requests
REQUEST_COUNTER = Counter('order_service_requests', 'Number of requests to order service')

@app.route('/')
def home():
    REQUEST_COUNTER.inc()
    return jsonify({"message": "Welcome to the Order Service"})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
