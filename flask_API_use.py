import requests

url = "http://127.0.0.1:5000/predict"
symptoms = {"symptoms": [1, 1, 0, 1]}  # Example symptom values
response = requests.post(url, json=symptoms)
print(response.json())
