def collect_chars(word, rooms):
    # Menghitung berapa kali kata harus diulang untuk mengisi semua ruangan
    repeat_times = rooms // len(word)

    # Mengulang kata sebanyak repeat_times dan menambahkan sisa karakter
    result = word * repeat_times + word[:rooms % len(word)]

    return result

# Test cases
print(collect_chars("alta", 10))          # altaaltaal
print(collect_chars("sepulsa", 20))       # sepulsasepulsasepuls
print(collect_chars("sepulsa mantap", 20))# sepulsa mantapsepuls
