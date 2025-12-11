import subprocess, time

def start_testing_agent():
    while True:
        print("[Testing] Running tests...")
        subprocess.call(["pytest","-q"])
        time.sleep(20)
