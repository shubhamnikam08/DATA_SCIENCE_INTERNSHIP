import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Visualize locations on a map using folium
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=10)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(restaurant_map)

restaurant_map.save('restaurant_locations_map.html')


# Distribution of restaurants across different cities or countries
plt.figure(figsize=(8, 5))
# There are many cities names present in the data, so i select only the top 10 cities
sns.countplot(y = df['City'], order=df.City.value_counts().iloc[:10].index)
plt.xlabel('Number of Restaurants')
plt.ylabel('Name of Cities')
plt.title('Distribution of Restaurants Across Cities')
plt.show()


# Determine if there is any correlation between the restaurant's location and its rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=df, palette='viridis', size='Aggregate rating', sizes=(10, 200))
plt.title('Correlation Between Restaurant Location and Rating')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Rating')
plt.show()