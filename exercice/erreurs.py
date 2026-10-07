import requests

try:
    response = requests.get("http://localhost:11434", timeout=5)
    print("Ollama répond :", response.text)
except requests.exceptions.ConnectionError:
    print("Erreur : Ollama n'est pas démarré.")