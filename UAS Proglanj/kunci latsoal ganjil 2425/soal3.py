"""
Sebuah rumah makan menyediakan beberapa menu berikut:
Makanan:
- Nasi Telur Cengeh Gedang, harga 25000
- Nasi Pelalah Kima, harga 40000
- Pencok Lendong, harga 25000
- Pencok Sagu, harga 20000
Minuman:
- Es Kenyamen Madu, 11000
- Es Beluluk, 12500 
Buatlah class Menu dan object yang merepresentasikan seluruh menu yang ada
"""

class Menu:
    def __init__(self,nama,jenis,harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

cengeh = Menu("Nasi Telur Cengeh Gedang","makanan",25000)
kima = Menu("Nasi Pelalah Kima","makanan",40000)
pck_lendong = Menu("Pencok Lendong","makanan",25000)
pck_sagu = Menu("Pencok Sagu","makanan",20000)
kenyamen = Menu("Es Kenyamen Madu","minuman",11000)
beluluk = Menu("Es Beluluk","minuman",12500)