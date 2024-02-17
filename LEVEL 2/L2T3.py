import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



# Load the dataset
data = pd.read_csv('Dataset.csv')

# Extracting additional features from the existing columns, such as the length of the restaurant name or address
data['Restaurant Name Length'] = data['Restaurant Name'].apply(len)

# Create a new column for the length of restaurant addresses
data['Address Length'] = data['Address'].apply(len)

# Display the updated DataFrame
print(data.head())
     
# Creating new features like "Has Table Booking" or "Has Online Delivery" by encoding categorical variables
data['Has Table Booking'] = np.where(data['Has Table booking'] == 'Yes', 1, 0)
data['Has Online Delivery'] = np.where(data['Has Online delivery'] == 'Yes', 1, 0)


# Display the updated DataFrame
print(data.head())