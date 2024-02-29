berat = int(input("berat"))
jarak = int(input("jarak"))
tarifberat = 0 
tarifjarak = 0 
if berat >= 1 and berat <= 20:
    tarifberat = 10000
elif berat >= 21 and berat <=30: 
    tarifberat = 15000
elif berat >= 31 and berat <=60:
    tarifberat = 20000
elif berat >60:
    tarifberat = 45000
else:
    print("masukan angka diatas 0")

if jarak >= 1 and jarak <= 5: 
    tarifjarak = 2000
elif jarak >= 6 and jarak <= 15: 
    tarifjarak = 5000
elif jarak >= 16 and jarak <=30: 
    tarifjarak = 10000
elif jarak >30: 
    tarifjarak = 15000 
else: 
    print("masukan angka diatas 0")

total=tarifberat+tarifjarak 
print(total)