import os
from jinja2 import Template

BACKEND_TEMPLATE = Template("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API OK"}
""")

def start_backend_agent(bus):
    q = bus.subscribe("agent_jobs")
    print("[Backend Agent] Subscribed to agent_jobs")
    while True:
        job = q.get()
        if job.get("type") == "generate_backend":
            # create generated backend scaffold
            os.makedirs("generated/backend", exist_ok=True)
            with open("generated/backend/__init__.py", "w", encoding="utf-8") as f:
                f.write("# generated backend package\n")
            code = BACKEND_TEMPLATE.render()
            with open("generated/backend/app.py", "w", encoding="utf-8") as f:
                f.write(code)
            # write a simple test file
            with open("generated/backend/test_generated_api.py", "w", encoding="utf-8") as f:
                f.write(
                    "def test_generated_app_import():\n"
                    "    import generated.backend.app as app\n"
                    "    assert hasattr(app, 'app')\n"
                )
            print("[Backend Agent] Generated backend API and test")
