import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Contoh data

df = pd.read_csv('house_listings.csv')

# Inisialisasi OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Kolom yang akan di-encode
columns_to_encode = ['category', 'title_deed', 'repair', 'mortgage']

# Melakukan fit dan transform data
encoded_data = encoder.fit_transform(df[columns_to_encode])

# Mengubah hasil encoding menjadi DataFrame
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(columns_to_encode))

encoded_df