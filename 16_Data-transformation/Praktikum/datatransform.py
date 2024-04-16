import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Membaca data dari file CSV
df = pd.read_csv('house_listings.csv')

# Menghapus semua karakter non-numerik kecuali titik desimal
df['price_1m2'] = df['price_1m2'].str.replace(r'[^\d.]+', '', regex=True)
df['price'] = df['price'].str.replace(r'[^\d.]+', '', regex=True)

# Membersihkan spasi di dalam nilai
df['price_1m2'] = df['price_1m2'].str.strip()
df['price'] = df['price'].str.strip()

# Konversi kolom 'price' dan 'price_1m2' ke tipe data numerik
df['price'] = df['price'].astype(float)
df['price_1m2'] = df['price_1m2'].astype(float)

# Normalisasi data harga rumah dan harga per meter persegi secara terpisah
scaler_price = MinMaxScaler()
scaler_price_1m2 = MinMaxScaler()

df['price_normalized'] = scaler_price.fit_transform(df[['price']])
df['price_1m2_normalized'] = scaler_price_1m2.fit_transform(df[['price_1m2']])

# Menampilkan hasil
print("Dataframe setelah normalisasi:")
print ('')
df[['price', 'price_1m2_normalized']].head()