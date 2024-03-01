def cek_anagram(kata1, kata2):
    # Mengurutkan huruf-huruf dalam kata-kata tersebut
    sorted_kata1 = sorted(kata1)
    sorted_kata2 = sorted(kata2)
    
    # Memeriksa apakah kata-kata tersebut memiliki urutan huruf yang sama setelah diurutkan
    if sorted_kata1 == sorted_kata2:
        return "Anagram"
    else:
        return "Bukan Anagram"

# Input
kata_pertama = input("Kata pertama: kasur").lower()
kata_kedua = input("Kata kedua: pulsa ").lower()

# Output
print("Output:")
print(cek_anagram(kata_pertama, kata_kedua))
