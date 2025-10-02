import subprocess
import json

def ask_ollama(prompt: str, model: str = "llama3") -> str:
    """Send a prompt to Ollama and get response"""
    process = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    return process.stdout.decode().strip()
