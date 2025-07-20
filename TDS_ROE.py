import pandas as pd

# Load data
df = pd.read_csv(r"C:\Users\agile\Downloads\retail_data.csv")

# Define the pairs to analyze
pairs = [
    ("Avg_Basket", "Footfall"),
    ("Avg_Basket", "Promo_Spend"),
    ("Footfall", "Promo_Spend")
]

# Calculate correlations
correlations = {
    f"{a}-{b}": df[a].corr(df[b])
    for a, b in pairs
}

# Find pair with strongest (absolute) correlation
strongest_pair = max(correlations, key=lambda k: abs(correlations[k]))

# Prepare the output dict
result = {
    "pair": strongest_pair,
    "correlation": round(correlations[strongest_pair], 2)
}

# Write to JSON file
import json
with open("correlation.json", "w") as f:
    json.dump(result, f)

print(result)