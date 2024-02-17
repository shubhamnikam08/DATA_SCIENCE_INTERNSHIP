import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
data = pd.read_csv("Dataset.csv")  # Replace "your_dataset.csv" with the actual file path

# Step 3: Explore the dataset
print("Number of rows and columns:", data.shape)
print(data.head())
print(data.info())
print(data.describe())

# Step 4: Check for missing values
print("Missing values per column:")
print(data.isnull().sum())

# Step 5: Data type conversion (if necessary)
# For example, if a column contains numeric values but is stored as object, you can convert it to numeric type:
# data['column_name'] = pd.to_numeric(data['column_name'], errors='coerce')

# Step 6: Analyze the distribution of the target variable
plt.figure(figsize=(8, 6))
sns.histplot(data['Aggregate rating'], bins=20, kde=True)
plt.title("Distribution of Aggregate rating")
plt.xlabel("Aggregate rating")
plt.ylabel("Frequency")
plt.show()

# Check for class imbalances
print("Class distribution of Aggregate rating:")
print(data['Aggregate rating'].value_counts())
