import pandas as pd

# Sample dataset: Symptoms and corresponding disease
data = {
    "Fever": [1, 0, 1, 1, 0],
    "Cough": [1, 1, 0, 1, 1],
    "Fatigue": [1, 1, 0, 1, 1],
    "Headache": [0, 1, 1, 0, 1],
    "Disease": ["Flu", "COVID-19", "Malaria", "Flu", "COVID-19"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV file
df.to_csv("health_data.csv", index=False)

print("CSV file 'health_data.csv' created successfully!")
