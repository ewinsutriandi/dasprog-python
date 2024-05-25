mk = {
    "kode"  : "FTK6201",
    "nama"  : "Dasar Pemrograman",
    "sks"   : 3,
    "wajib" : True
}

# Loop untuk mendapatkan seluruh key pada dictionary
for k in mk:
    print(k)
    
# Loop untuk mendapatkan seluruh key dan value sekaligus
for k,v in mk.items():
    print(f"Key {k} pada dictionary bernilai: {v}")

