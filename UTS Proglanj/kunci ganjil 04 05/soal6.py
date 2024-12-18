"""
Sebuah tempat rekreasi memberikan harga tiket yang berbeda kepada pengunjung sesuai dengan usia pengunjung tersebut. 
Harga tiket tersebut adalah:
Bayi usia kurang dari 1 tahun, gratis
Anak usia 1-5 tahun, 15.000
Anak usia 6-10 tahun, 20.000
Remaja dan dewasa di atas usia 11th, 30.000

Buatlah sebuah fungsi yang menerima input parameter usia calon pengunjung kemudian mengembalikan harga tiket yang harus dibayar.

Buat program yang meminta input nama dan usia pengunjung. Program kemudian mencetak nama pengunjung serta berapa harga tiket yang harus dibayar dengan memanfaatkan fungsi yang sudah dibuat sebelumnya.

"""

def harga_tiket(usia):
    if usia >= 11:
        harga = 30000
    elif usia >= 6:
        harga = 20000
    elif usia >= 1:
        harga = 15000
    else:
        harga = 0
    return harga

nama = input("Masukkan nama pengunjung: ")
usia = int(input("Masukkan usia pengunjung: "))
harga = harga_tiket(usia)

print(f"{nama} harus membayar tiket sebesar {harga} rupiah")