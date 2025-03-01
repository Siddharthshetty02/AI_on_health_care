import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("dataset.csv")

# Split data into features (X) and labels (y)
X = df.drop(columns=["Disease"])
y = df["Disease"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("disease_model.pkl", "wb"))
print("Model trained and saved!")
