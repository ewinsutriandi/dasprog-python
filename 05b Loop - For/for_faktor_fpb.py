'''
Buatlah program yang menerima dua buah bilangan bulat
kemudian menghitung FPBnya dengan terlebih dahulu 
mencari seluruh faktor dari masing-masing bilangan
'''

# Input bilangan
b1 = int(input("Bil 1: "))
b2 = int(input("Bil 2: "))

# Cari faktor b1 dan b2
faktor_b1 = []
faktor_b2 = []

for i in range(1,b1):
    if b1 % i == 0:
        faktor_b1.append(i)

for i in range(1,b2):
    if b2 % i == 0:
        faktor_b2.append(i)

print(f"faktor dari {b1}: {faktor_b1}")
print(f"faktor dari {b2}: {faktor_b2}")

for f in faktor_b1:
    if f in faktor_b2: # faktor persekutuan
        fpb = f # di akhir loop akan terisi FPB karena loop dari kecil ke besar

print(f"FPB dari {b1} & {b2} adalah {fpb}")