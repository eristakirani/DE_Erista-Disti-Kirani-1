import pandas as pd

# Membuat DataFrame
df = pd.read_csv('house_listings.csv')

# Menghitung rata-rata, median, dan modus untuk 'category' dan 'room_number'
mean_room_number = df['room_number'].mean()
median_room_number = df['room_number'].median()
mode_room_number = df['room_number'].mode()[0]

# Output
print("Rata-rata jumlah kamar:", mean_room_number)
print("Median jumlah kamar:", median_room_number)
print("Modus jumlah kamar:", mode_room_number)

# Agregasi berdasarkan 'category'
aggregated_data = df.groupby('category').agg({
    'room_number': ['mean', 'median']
}).reset_index()

print(aggregated_data)