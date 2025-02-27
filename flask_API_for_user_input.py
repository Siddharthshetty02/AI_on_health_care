from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
with open("health_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI Healthcare Diagnosis API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Expecting JSON input
    symptoms = np.array(data["symptoms"]).reshape(1, -1)
    prediction = model.predict(symptoms)[0]
    return jsonify({"Predicted Disease": prediction})

if __name__ == "__main__":
    app.run(debug=True)
