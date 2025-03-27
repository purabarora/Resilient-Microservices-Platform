import random
import time
import subprocess

# List of services to simulate a failure on
services = ["user-service", "order-service"]

# Wait for a random delay between 30 and 60 seconds
delay = random.randint(30, 60)
print(f"Chaos Monkey will strike in {delay} seconds...")
time.sleep(delay)

# Randomly choose a service to stop
target = random.choice(services)
print(f"Chaos Monkey is stopping the {target} container...")

# Execute the docker-compose command to stop the target container
subprocess.run(["docker-compose", "stop", target])
print(f"{target} container has been stopped.")
