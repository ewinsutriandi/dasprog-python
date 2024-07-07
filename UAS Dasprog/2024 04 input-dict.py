'''
Data berikut adalah sebuah tabel yang berisi data beberapa bandar udara di Indonesia.

Buatlah sebuah variabel berisi dictionary yang menampung seluruh data tersebut dengan IATA codenya sebagai key dictionary.
Minta user untuk memberikan input berupa kode IATA
Gunakan kode IATA tersebut untuk menampilkan identitas bandara yang bersesuaian


Contoh:
User memasukkan BDO maka program kemudian menampilkan: 
BDO, Bandar Udara Husein Sastranegara, Bandung, Provinsi Jawa Barat

'''

daftar_bandara = {
    "CGK" : {"nama":"Bandar Udara Internasional Soekarno Hatta","lokasi":"Tangerang, Provinsi Banten"},
    "SUB" : {"nama":"Bandar Udara Internasional Juanda","lokasi":"Surabaya, Provinsi Jawa Timur"},
    "LOP" : {"nama":"Bandar Udara Internasional Lombok","lokasi":"Praya, Provinsi NTB"},
    "DPS" : {"nama":"Bandar Udara Internasional I Gusti Ngurah Rai","lokasi":"Denpasar, Provinsi Bali"},
    "SRG" : {"nama":"Bandar Udara Ahmad Yani","lokasi":"Semarang, Provinsi Jawa Timur"},
    "BDO" : {"nama":"Bandar Udara Husein Sastranegara","lokasi":"Bandung, Provinsi Jawa Barat"},
}

kode = input("Masukkan kode bandara: ")

if kode in daftar_bandara:
    bandara = daftar_bandara[kode]
    print(f"{kode}, {bandara['nama']}, {bandara['lokasi']}")
else:
    print(f"Bandara dengan kode {kode} tidak ditemukan")
    