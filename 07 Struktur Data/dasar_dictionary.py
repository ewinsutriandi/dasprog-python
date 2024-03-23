# deklarasi
upin = {
    "nama lengkap" : "Aruffin bin Abdul Salam",
    "tinggi" : 110,
    "berat"  : 17
}

mhs = {
    "nim" : "1234567",
    "nama" : "Asep Davidson",
    "prodi" : "Teknik Informatika",
    "thn masuk" : 2021,
    "cuti" : False
}

proglanj = {
    "kode" : "TI6303",
    "nama" : "Pemrograman Lanjut",
    "sks" : 3
}
# akses elemen pada dictionary menggunakan key
print(upin["nama lengkap"],upin["tinggi"])
print(mhs["nim"],mhs["nama"],mhs["prodi"],mhs["thn masuk"])
print(f"Mata kuliah {proglanj['nama']} memiliki bobot {proglanj['sks']} SKS")

# update elemen
mhs["prodi"] = "Ilmu Komputer"
print(mhs)

# tambah elemen 
mhs["asal"] = "Pancor"
print(mhs)

# loop
for k in mhs:
    print(k,":",mhs[k])

for k,v in mhs.items():
    print(k,v)

    

    