'''
Buatlah sebuah program yang meminta user memasukkan sebuah nilai integer terus menerus,
sampai user memasukkan nilai 0. 
Di akhir program, tampilkan rata-rata nilai yang diinput oleh user
'''

lanjut = True
jumlah_nilai = 0
banyak_nilai = 0

while lanjut:
    nilai = int(input("Masukkan nilai: "))
    if nilai == 0:
        lanjut = False
    else:
        jumlah_nilai += nilai
        banyak_nilai += 1

rerata = jumlah_nilai / banyak_nilai

print(f"Rata-rata nilai: {rerata}")

