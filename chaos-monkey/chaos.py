from kubernetes import client, config
import random
import time

# List of services to target
services = ["user-service", "order-service"]

# Load Kubernetes configuration inside the cluster
config.load_incluster_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

def chaos_monkey():
    print("Chaos Monkey will strike in 30 seconds...")
    time.sleep(30)

    # Choose a random service to kill
    service_to_kill = random.choice(services)
    print(f"Chaos Monkey is stopping a pod from {service_to_kill}...")

    try:
        # Get all pods for the selected service
        pods = v1.list_namespaced_pod(namespace="default", label_selector=f"app={service_to_kill}").items

        if pods:
            # Choose a random pod to kill
            pod_to_kill = random.choice(pods)
            pod_name = pod_to_kill.metadata.name

            # Delete the pod
            v1.delete_namespaced_pod(name=pod_name, namespace="default")
            print(f"✅ Pod {pod_name} deleted successfully!")
        else:
            print(f"⚠️ No pods found for {service_to_kill}.")
    except Exception as e:
        print(f"⚠️ Error stopping pod: {e}")

if __name__ == "__main__":
    chaos_monkey()
