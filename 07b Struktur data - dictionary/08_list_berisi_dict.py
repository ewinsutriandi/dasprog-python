daftar_mhs = [
    {
        "nim"  : "13424001",
        "nama"  : "Soleh Rahmat",
        "thn_masuk"   : 2024
    },
    {
        "nim"  : "13424002",
        "nama"  : "Dinda Ceria",
        "thn_masuk"   : 2024
    },
    {
        "nim"  : "13424003",
        "nama"  : "Syakila Onila",
        "thn_masuk"   : 2024
    },
    {
        "nim"  : "13424004",
        "nama"  : "Fernando Maldini",
        "thn_masuk"   : 2024
    },
]

for mhs in daftar_mhs:
    print(f"{mhs['nama']} dengan NIM {mhs['nim']} masuk tahun {mhs['thn_masuk']}")