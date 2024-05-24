mk = {
    "kode" : "FTK6201",
    "nama" : "Dasar Pemrograman",
    "sks"  : 3
}
print(f"Mata kuliah {mk['nama']} memiliki beban {mk['sks']} SKS")

mk["sks"] = 2 # ganti nilai dengan key sks
print(f"Mata kuliah {mk['nama']} memiliki beban {mk['sks']} SKS")