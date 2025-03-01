import pandas as pd

# Define the data (Symptoms: 1 = Present, 0 = Absent)
data = {
    "Fever": [1, 1, 0, 1, 0, 1],
    "Cough": [1, 1, 1, 0, 1, 0],
    "Fatigue": [1, 0, 1, 1, 0, 1],
    "Headache": [0, 1, 1, 0, 1, 0],
    "Sore Throat": [1, 1, 0, 1, 0, 1],
    "Shortness of Breath": [0, 1, 1, 0, 1, 0],
    "Disease": ["Flu", "COVID-19", "Common Cold", "Migraine", "Asthma", "Dengue"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
csv_filename = "dataset.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' has been created successfully!")
