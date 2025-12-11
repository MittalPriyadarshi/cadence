import sys, os
import threading
from bus import Bus

# Ensure current directory is in Python path
sys.path.append(os.path.abspath("."))

# Import all agent entry points
from agents.ado_connector import start_ado_connector
from agents.coordinator import start_coordinator
from agents.backend_agent import start_backend_agent
from agents.database_agent import start_database_agent
from agents.testing_agent import start_testing_agent
from agents.legacy_agent import start_legacy_agent
from agents.prompt_refinement_agent import start_prompt_refinement_agent
from agents.frontend_agent import start_frontend_agent
from agents.monitoring_agent import start_monitoring_agent

def main():
    # Create a single in-memory Bus for communication
    bus = Bus()

    # Create threads for all agents, passing bus
    threads = [
        threading.Thread(target=start_ado_connector, args=(bus,), name="ADO Connector"),
        threading.Thread(target=start_coordinator, args=(bus,), name="Coordinator"),
        threading.Thread(target=start_backend_agent, args=(bus,), name="Backend Agent"),
        threading.Thread(target=start_database_agent, args=(bus,), name="Database Agent"),
        threading.Thread(target=start_testing_agent, args=(bus,), name="Testing Agent"),
        threading.Thread(target=start_legacy_agent, args=(bus,), name="Legacy Agent"),
        threading.Thread(target=start_prompt_refinement_agent, args=(bus,), name="Prompt Refinement Agent"),
        threading.Thread(target=start_frontend_agent, args=(bus,), name="Frontend Agent"),
        threading.Thread(target=start_monitoring_agent, args=(bus,), name="Monitoring Agent"),
    ]

    # Start all threads
    for t in threads:
        t.daemon = True  # allow exit on main thread termination
        t.start()

    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[Main] Stopping CADENCE PoC...")

if __name__ == "__main__":
    main()
