"""
Nilai tukar Dolar Amerika Serikat adalah 16.000 rupiah

Buatlah fungsi yang menerima input parameter berupa nilai uang dalam Dolar AS kemudian mengembalikan nilai uang tersebut dalam rupiah.

Berikan contoh cara menggunakan fungsi tersebut

"""

def nilai_tukar_usd(nilai_usd):
    kurs_usd = 16000 # 1 USD = 16000 IDR
    nilai_tukar = kurs_usd * nilai_usd
    return nilai_tukar

nilai_3USD = nilai_tukar_usd(3)
print(f"3 USD setara dengan {nilai_3USD} rupiah")