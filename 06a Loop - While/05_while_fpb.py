b1 = int(input("Bil 1: "))
b2 = int(input("Bil 2: "))

fpb = 1
pencacah = 2

if b2 > b1:
  batas = b1
else:
  batas = b2

while pencacah <= batas:
  if b1 % pencacah == 0 and b2 % pencacah == 0:
    fpb = pencacah
  pencacah += 1    

print(f"FPB dari {b1} & {b2} adalah {fpb}")

'''
Contoh dibuat untuk mendemonstrasikan cara menggunakan perulangan while
Untuk mencari FPB, terdapat banyak algoritma lain yang lebih efisien
'''