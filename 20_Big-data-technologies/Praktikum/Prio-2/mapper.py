#!/usr/bin/env python3
import sys

class CustomMeanCalculatorMapper:
    
    @staticmethod
    def process_input_and_calculate_mean(line):
        try:
            # Memisahkan baris input menjadi nilai-nilai yang dipisahkan oleh koma
            values = line.strip().split(',')
            
            # Menghitung total nilai dan jumlah elemen
            total = sum(map(float, values))
            count = len(values)
            
            # Outputkan total nilai dan jumlah elemen sebagai pasangan (kunci, nilai)
            print(f"{total}\t{count}")
        except Exception as e:
            # Menangani kesalahan jika ada
            sys.stderr.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    # Membaca input dari standar input dan memprosesnya dengan mapper
    for line in sys.stdin:
        CustomMeanCalculatorMapper.process_input_and_calculate_mean(line)