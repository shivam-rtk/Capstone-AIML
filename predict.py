import requests

ride = {
    "cylinders": 0.4,
    "displacement": 0.8,
    "weight": 1,
    "acceleration": 0.9
}

url = 'http://localhost:9696/predict'

try:
    response = requests.post(url, json=ride)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit(1)
