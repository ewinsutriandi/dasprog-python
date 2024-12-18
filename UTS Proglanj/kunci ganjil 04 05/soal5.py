"""
Panjang 1 m = 100 cm

Buat sebuah fungsi yang melakukan konversi dari suatu nilai satuan ke nilai satuan lainnya. Fungsi tersebut menerima input parameter nilai, satuan asal, dan tujuan kemudian mengembalikan nilai hasil konversinya

Cth: 
Parameter masukan 3,m,cm kemudian fungsi mengembalikan nilai 300
Parameter masukan 150,cm,m kemudian fungsi mengembalikan nilai 1.5

Berikan contoh cara menggunakan fungsi tersebut

"""

def konversi(nil,dari,ke): 
    if dari == "cm" and ke == "m":
        konversi = nil / 100
    elif dari == "m" and ke=="cm":
        konversi = nil * 100
    else:
        konversi = "Satuan tidak dikenali"
    return konversi

nil_m = 2.5
nil_cm = konversi(nil_m,"m","cm")
print(f"{nil_m} meter = {nil_cm} cm")