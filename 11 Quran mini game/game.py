import json
import random

file = open("surat_alquran.json",encoding="utf8") # load file
daftar_surat = json.load(file) # konversi isi file (json) ke dictionary

daftar_surat = list(daftar_surat.values()) # konversi dictionary menjadi list
surat_10 = random.sample(daftar_surat,k=10) # ambil sampel 10 surat secara acak

pilihan_salah = []
for surat in surat_10:
    pilihan_salah.append(surat['arti_nama'])

skor = 0
for surat in surat_10:
    print(f"Arti nama dari surat {surat['nama']} adalah?: ") # cetak pertanyaan
    # siapkan pilihan jawaban
    jawaban_benar = surat['arti_nama']
    pilihan_jawaban = random.sample(pilihan_salah,k=2) # tambahkan jawaban salah
    pilihan_jawaban.append(jawaban_benar) # tambahkan jawaban benar
    random.shuffle(pilihan_jawaban) # acak urutan
    peta_jawaban = {"a":pilihan_jawaban[0],"b":pilihan_jawaban[1],"c":pilihan_jawaban[2]}
    # cetak pilihan jawaban
    print(f"Pilih a. {pilihan_jawaban[0]} b. {pilihan_jawaban[1]} c. {pilihan_jawaban[2]}")
    
    respon_user = input("a/b/c: ") # ambil respon user (a,b,c)
    jawaban_user = peta_jawaban[respon_user]

    if jawaban_user == jawaban_benar:
        skor += 1
        print(f"Benar! Skor anda sekarang {skor}")
    else:
        print(f"Salah! Jawaban yang benar adalah: {jawaban_benar}")

print(f"Permainan berakhir, anda mendapatkan skor akhir {skor}")