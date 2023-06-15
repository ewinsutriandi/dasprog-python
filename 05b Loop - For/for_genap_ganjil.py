'''
Buatlah sebuah program yang menerima sebuah nilai (integer), misalkan n
Kemudian mencetak n baris dengan pola sebagai berikut

Untuk n = 3
ganjil
genap
ganjil

Untuk n = 5
ganjil
genap
ganjil
genap
ganjil
'''

n = int(input("Masukkan sebuah nilai: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

