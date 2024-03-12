def group_numbers(numbers, target):
    # Inisialisasi list kosong untuk menyimpan kelompok bilangan
    groups = [[] for _ in range(target)]

    # Menyusun bilangan ke dalam kelompok berdasarkan target kelipatan
    for num in numbers:
        group_index = num % target
        groups[group_index].append(num)

    return groups

# Test cases
print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # [[3, 6, 9], [1, 4, 7], [2, 5, 8]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5)) # [[15, 20, 75, 30, 45], [23, 19]]
