import requests

url = "http://127.0.0.1:5000/predict"
data = {"symptoms": [1, 1, 0, 1]}  
response = requests.post(url, json=data)
print(response.json())  # Output: {"Predicted Disease": "Flu"}

# Chatbot test
chat_response = requests.post("http://127.0.0.1:5000/chat", json={"message": "I have a fever"})
print(chat_response.json())  # Output: {"response": "Fever can be caused by infections. Please rest and drink fluids."}
