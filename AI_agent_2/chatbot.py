import random

responses = {
    "hello": ["Hi! How can I assist you?", "Hello! What do you need help with?"],
    "fever": ["Fever can be caused by infections. Please rest and drink fluids."],
    "covid": ["If you suspect COVID-19, get tested and isolate if necessary."],
    "doctor": ["I recommend seeing a doctor if symptoms persist."],
    "bye": ["Goodbye! Stay healthy!"]
}

def get_response(user_input):
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return "I'm not sure, please consult a medical professional."
