daftar_mhs = {
    "13424001" : {
        "nama"  : "Soleh Rahmat",
        "thn_masuk"   : 2024
    },
    "13424002" : {
        "nama"  : "Dinda Ceria",
        "thn_masuk"   : 2024
    },
    "13424003" : {
        "nama"  : "Syakila Onila",
        "thn_masuk"   : 2024
    },
    "13424004": {
        "nama"  : "Fernando Maldini",
        "thn_masuk"   : 2024
    },
}

for k,v in daftar_mhs.items():
    print(f"{v['nama']} dengan NIM {k} masuk tahun {v['thn_masuk']}")