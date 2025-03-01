from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained disease prediction model
model = pickle.load(open("disease_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")  # Serve the HTML page

@app.route("/predict", methods=["POST"])
def predict():
    """Handles symptom input and returns predicted disease"""
    try:
        data = request.json["symptoms"]  # Get symptoms from frontend
        prediction = model.predict([np.array(data)])  # Predict disease
        return jsonify({"Predicted Disease": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot messages"""
    user_message = request.json["message"]
    # Simulate chatbot response (Replace with actual AI model later)
    bot_response = f"I'm not a doctor, but I suggest drinking water for '{user_message}'"
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
