import pandas as pd

data = pd.DataFrame({
    "Name": [" Aftab ", "Pavan", "Arun ", "Aftab"],
    "Age": [21, 20, None, 20],
    "Marks": [85, 92, 110, 92]
})

print("--- RAW DATA ---")
print(data)

# 1. Remove leading/trailing spaces from strings
data["Name"] = data["Name"].str.strip()

# 2. Impute missing Age with mean
data["Age"] = data["Age"].fillna(data["Age"].mean())

# 3. Remove duplicate rows (e.g., second Aftab row)
data = data.drop_duplicates()

# 4. Filter out invalid marks (Keep marks strictly between 0 and 100)
data = data[(data["Marks"] > 0) & (data["Marks"] <= 100)]

print("\n--- PROCESSED DATA ---")
print(data)
