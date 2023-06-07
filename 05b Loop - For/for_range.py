'''
For digunakan untuk melakukan eksekusi kode secara berulang
berdasarkan urutan nilai tertentu
'''
for i in range(3):
    print("Belajar perulangan")

'''
range dengan satu parameter
range(a) menghasilkan urutan nilai dari 0 s..d a-1
'''
for i in range(3):
    print(f"Ini adalah perulangan ke-{i}")

'''
range dengan dua parameter
range(a,b) menghasilkan urutan nilai dari a s..d b-1
'''
for i in range(7,10):
    print(f"Ini adalah perulangan ke-{i}")

'''
range dengan tiga parameter
range(a,b,c) menghasilkan urutan nilai dari a s..d b-1, lompatan/step senilai c
'''
for i in range(2,12,3):
    print(f"Ini adalah perulangan ke-{i}")

'''
range dengan lompatan negatif
range(a,b,c), a > b, c < 0
'''
for i in range(11,0,-2):
    print(f"Ini adalah perulangan ke-{i}")