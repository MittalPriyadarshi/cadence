import time, json

def start_ado_connector(bus):
    """
    Periodically publishes a sample user story to the in-memory bus.
    """
    while True:
        # Load a sample story (or define inline)
        try:
            with open("sample-stories/sample_story.json", "r", encoding="utf-8") as f:
                story = json.load(f)
        except FileNotFoundError:
            # fallback sample story if file doesn't exist
            story = {
                "id": 1,
                "title": "Create backend API",
                "acceptance": ["API root returns JSON"]
            }

        msg = {"type": "ado_story", "payload": story, "confidence": 0.9}
        bus.publish("tasks", msg)
        print("[ADO] Published story to tasks")
        time.sleep(10)
