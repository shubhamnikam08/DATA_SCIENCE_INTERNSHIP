import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Convert 'Yes' to 1 and 'No' to 0 in 'Has Table booking' and 'Has Online delivery' columns
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})

# Determine the percentage of restaurants that offer table booking and online delivery
table_booking_percentage = (df['Has Table booking'].sum() / len(df)) * 100
online_delivery_percentage = (df['Has Online delivery'].sum() / len(df)) * 100

print(f"Percentage of Restaurants with Table Booking: {table_booking_percentage:.2f}%")
print(f"Percentage of Restaurants with Online Delivery: {online_delivery_percentage:.2f}%")



# Compare the average ratings of restaurants with table booking and those without
avg_rating_with_table_booking = df[df['Has Table booking'] == 1]['Aggregate rating'].mean()
avg_rating_without_table_booking = df[df['Has Table booking'] == 0]['Aggregate rating'].mean()

print(f"Average Rating for Restaurants with Table Booking: {avg_rating_with_table_booking:.2f}")
print(f"Average Rating for Restaurants without Table Booking: {avg_rating_without_table_booking:.2f}")

# Analyze the availability of online delivery among restaurants with different price ranges
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Has Online delivery', data=df, hue='Price range', palette='Set3', dodge=False)
plt.title('Availability of Online Delivery Across Different Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Online Delivery Availability (1: Yes, 0: No)')
plt.legend(title='Price Range', loc='upper left')
plt.show()

print("************************************************************************")
# Availability of online delivery among restaurants with different price ranges
# Select price ranges
price_ranges = df['Average Cost for two'].apply(lambda x: 'Low' if x < 500 else 'Medium' if 500 <= x <= 1000 else 'High')
online_delivery_by_price_range = df.groupby(price_ranges)['Has Online delivery'].value_counts(normalize=True).unstack()

# Display results
print("Online Delivery Availability by Price Range:")
print(online_delivery_by_price_range)