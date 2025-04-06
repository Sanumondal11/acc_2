
# core/embedding.py

import subprocess

def generate_embedding(text):
    prompt = f"Return a 10-dimensional float vector representing the semantic embedding of this input: {text}"
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=15
    )
    output = result.stdout.decode().strip()
    try:
        return [float(x) for x in output.split()[:10]]
    except Exception:
        return [0.0] * 10
