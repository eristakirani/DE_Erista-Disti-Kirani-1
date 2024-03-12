def get_breads(breads, flour_stock):
    # List untuk menyimpan nama roti yang dapat dibuat
    available_breads = []

    # Iterasi melalui setiap jenis roti
    for bread in breads:
        # Cek apakah tepung yang dibutuhkan untuk roti tersebut dapat dipenuhi
        if bread['flour'] <= flour_stock:
            available_breads.append(bread['name'])
            flour_stock -= bread['flour']  # Kurangi tepung yang digunakan

    return available_breads

bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
    {"name": "pancake", "flour": 15},
    {"name": "waffle", "flour": 25},
    {"name": "bagel", "flour": 15},
    {"name": "cupcake", "flour": 15},
    {"name": "choco chips", "flour": 10},
    {"name": "mini puff", "flour": 5},
    {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))  # ['mini puff', 'cupcake', 'donut']
print(get_breads(bread2, 75))   # ['mini puff', 'choco chips', 'pancake', 'bagel', 'cupcake']
