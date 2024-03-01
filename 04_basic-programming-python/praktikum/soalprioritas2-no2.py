def hitung_skor_budget(budget):
    if budget <= 50:
        return 4
    elif budget <= 80:
        return 3
    elif budget <= 100:
        return 2
    else:
        return 1

def hitung_skor_waktu(waktu):
    if waktu <= 20:
        return 10
    elif waktu <= 30:
        return 5
    elif waktu <= 50:
        return 2
    else:
        return 1

def hitung_skor_kesulitan(kesulitan):
    if kesulitan <= 3:
        return 10
    elif kesulitan <= 6:
        return 5
    elif kesulitan <= 10:
        return 1
    else:
        return 0

def tentukan_prioritas(budget, waktu, kesulitan):
    skor_budget = hitung_skor_budget(budget)
    skor_waktu = hitung_skor_waktu(waktu)
    skor_kesulitan = hitung_skor_kesulitan(kesulitan)
    
    total_skor = skor_budget + skor_waktu + skor_kesulitan
    
    if 24 <= total_skor <= 17:
        return "High"
    elif 16 <= total_skor <= 10:
        return "Medium"
    elif 9 <= total_skor <= 3:
        return "Low"
    else:
        return "Impossible"

input_budget = 40
input_waktu = 25
input_kesulitan = 5
print("Input:")
print("Budget:", input_budget)
print("Waktu pengerjaan:", input_waktu)
print("Tingkat kesulitan:", input_kesulitan)
print("Output:", tentukan_prioritas(input_budget, input_waktu, input_kesulitan))

input_budget = 51
input_waktu = 10
input_kesulitan = 3
print("\nInput:")
print("Budget:", input_budget)
print("Waktu pengerjaan:", input_waktu)
print("Tingkat kesulitan:", input_kesulitan)
print("Output:", tentukan_prioritas(input_budget, input_waktu, input_kesulitan))


