import json
import random

file = open("11 Quran mini game/surat_alquran.json")
daftar_surat = json.load(file) # load json file ke dalam dictionary
daftar_surat = list(daftar_surat.values()) # konversi dictionary ke list
surat_terpilih = random.sample(daftar_surat, k=10) # ambil 10 surat secara acak

def susun_pilihan_ganda(surat):
    pil_benar = surat['arti_nama']
    kandidat_pilihan = []
    for s in daftar_surat:
        kandidat_pilihan.append(s['arti_nama'])
    kandidat_pilihan.remove(pil_benar) # buang yg benar dari kandidat pilihan (akan ditambah kemudian)
    pil_ganda = random.sample(kandidat_pilihan,k=2) # tambahkan dua jawaban yg salah (dari surat lain)
    pil_ganda.append(pil_benar) # tambahkan jawaban yg benar
    random.shuffle(pil_ganda) # acak urutan pilihan
    peta_pilihan = {"a": pil_ganda[0], "b": pil_ganda[1], "c":pil_ganda[2] } # petakan dengan abjad a,b,c
    return peta_pilihan 

skor = 0
for surat in surat_terpilih:
    print(f"Arti dari nama surat {surat['nama']} adalah?")
    pilihan_ganda = susun_pilihan_ganda(surat)
    print(f"a. {pilihan_ganda['a']} b. {pilihan_ganda['b']} c. {pilihan_ganda['c']}")
    jwban = input("a/b/c?: ")
    jwban = pilihan_ganda[jwban]
    if jwban == surat["arti_nama"]:
        skor += 1
        print(f"Benar!")
    else:
        print(f"Salah! Jawaban yang benar adalah {surat['arti_nama']}") 

print(f"Permainan berakhir, skor anda {skor}")