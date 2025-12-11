import json

def start_coordinator(bus):
    """
    Subscribes to 'tasks' and delegates jobs to agents via in-memory bus.
    """
    q = bus.subscribe("tasks")
    print("[Coordinator] Subscribed to tasks")
    
    while True:
        data = q.get()  # wait for task
        if data.get("type") == "ado_story":
            # delegate backend generation
            job = {"type": "generate_backend", "payload": data["payload"], "confidence": 0.95}
            bus.publish("agent_jobs", job)
            print("[Coordinator] Delegated backend job")

