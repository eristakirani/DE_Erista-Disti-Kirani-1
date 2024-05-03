#!/usr/bin/env python3
import sys

class CustomMeanCalculatorReducer:
    
    def __init__(self):
        # Inisialisasi total jumlah nilai dan total jumlah elemen
        self.total_sum = 0
        self.total_count = 0
    
    def process_input_and_update_totals(self, line):
        try:
            # Mendapatkan total nilai dan jumlah elemen dari baris input
            total, count = map(float, line.strip().split('\t'))
            
            # Menambahkan total nilai dan jumlah elemen ke variabel total
            self.total_sum += total
            self.total_count += count
        except Exception as e:
            # Menangani kesalahan jika ada
            sys.stderr.write(f"Error: {str(e)}\n")
    
    def calculate_mean(self):
        # Menghitung rata-rata dari total nilai dan total jumlah elemen
        return self.total_sum / self.total_count if self.total_count != 0 else 0

if __name__ == "__main__":
    # Membuat objek reducer
    custom_mean_calculator = CustomMeanCalculatorReducer()
    
    # Membaca input dari standar input dan memprosesnya dengan reducer
    for line in sys.stdin:
        custom_mean_calculator.process_input_and_update_totals(line)
    
    # Menghitung rata-rata dan mengeluarkannya sebagai output
    mean = custom_mean_calculator.calculate_mean()
    print("Rata-rata:", mean)