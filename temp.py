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
for i in range(b1,0,-1):
    if b1 % i == 0:
        faktor_b1.append(i)
for i in range(b2,0,-1):
    if b2 % i == 0:
        faktor_b2.append(i)
print(f"Faktor dari {b1}: {faktor_b1}")
print(f"Faktor dari {b2}: {faktor_b2}")
# Cari FPB
for f in faktor_b1:
    if f in faktor_b2:
        fpb = f
        break

print(f"FPB {b1} & {b2} adalah {f}")    
