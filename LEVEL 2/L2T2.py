import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Determining the most common price range among all the restaurants
most_common_price_range = df['Price range'].mode()[0]
print(f"Most Common Price Range: {most_common_price_range}")

# Calculating average rating for each price range
# Group by 'Price range' and calculate the average rating
avg_rating_by_price_range = df.groupby('Price range')['Aggregate rating'].mean()

# Display result
print("Average rating for each price range:")
print(round(avg_rating_by_price_range,3))


# Identifying the color that represents the highest average rating among different price ranges
# Find the price range with the highest average rating
highest_avg_rating_color = avg_rating_by_price_range.idxmax()

# Create the bar plot
plt.bar(avg_rating_by_price_range.index, avg_rating_by_price_range, color='orange')

# Set the color of the bar corresponding to the highest average rating to a distinct color (e.g., green)
plt.bar(highest_avg_rating_color, avg_rating_by_price_range[highest_avg_rating_color], color='black')

# Set labels
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.title('Average Rating by Price Range')

# Highlight the bar for the highest average rating
plt.show()