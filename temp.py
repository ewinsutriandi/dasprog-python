'''
buatlah program yang menerima  dua buah bil bulat kemudian menghitung FPBnya dengan terlebih dahulu mencari seluruh faktor dari masing-masing bilangan.
'''

# input bilangan
x = int(input("Masukan bilangan pertama:"))
y = int(input("masukan bilangan kedua:"))

#   cari faktor bil dan FPB
if x > y:
  bil_terkecil = y
else:
  bil_terkecil = x

for i in range(1,bil_terkecil+1): 
  if ( x % i == 0 ) and (y % i == 0):
     fpb = i

# Tampilkan
print(f" Faktor dari fpb adalh {fpb}")
  
