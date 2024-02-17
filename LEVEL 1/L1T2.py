import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset.csv")  # Replace "your_dataset.csv" with the actual file path

# Step 1: Calculate basic statistical measures for numerical columns
numerical_stats = data.describe()
print("Basic Statistical Measures for Numerical Columns:")
print(numerical_stats)

# Step 2: Explore the distribution of categorical variables
categorical_variables = ["Country Code", "City", "Cuisines"]
for column in categorical_variables:
    print(f"\nDistribution of {column}:")
    print(data[column].value_counts())

    # Optional: Visualize the distribution
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    
    # Increase the distance between the names
    plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels by 45 degrees
    plt.tight_layout()  # Adjust layout to prevent overlapping
    
    plt.show()

# Step 3: Identify the top cuisines and cities with the highest number of restaurants
top_cuisines = data['Cuisines'].value_counts().head(10)
print("\nTop Cuisines:")
print(top_cuisines)

top_cities = data['City'].value_counts().head(10)
print("\nTop Cities with the Highest Number of Restaurants:")
print(top_cities)
