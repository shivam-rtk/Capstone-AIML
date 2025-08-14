#test.py
import requests
 
ride = {
    "cylinders": 0.4,
    "displacement": 0.8,
    "weight": 1,
    "acceleration": 0.9
}
 
url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
