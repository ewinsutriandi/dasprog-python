'''
Contoh penggunaan fungsi pada permainan sederhana 2
Game Asmaul Husna
'''
import json
import random

def load_asmaul_husna():
    try:
        with open('08 Fungsi/10 asmaul_husna.json',encoding='utf-8') as f:
            d = json.load(f)
            return d["asmaul_husna"]
    except FileNotFoundError:
        print("File tidak ditemukan")

def tampilkan_deksripsi_permainan(n):
    ''' Fungsi untuk menampilkan petunjuk bermain'''
    print("ARTI ASMAUL HUSNA")
    print(f"Komputer akan memilih {n} nama dari 99 asmaul husna")
    print("Pilih arti yang benar untuk tiap nama")
    input("Tekan ENTER untuk memulai ")

def tampilkan_statistik_permainan(benar,salah):
    print("PERMAINAN BERAKHIR")
    print(f"Total soal: {benar + salah}")
    print(f"benar: {benar}, salah: {salah}")

def siapkan_pilihan(nama,asmaul_husna):
    kandidat_pilihan_salah = asmaul_husna.copy()
    jawaban_benar = nama["Indonesia"]
    kandidat_pilihan_salah.remove(nama) # buang jawaban benar dari kandidat jawaban salah
    kandidat_pilihan_salah = random.sample(kandidat_pilihan_salah,2) # siapkan dua jawaban salah
    pilihan_jawaban = [jawaban_benar] # buat list berisi jawaban benar
    pilihan_jawaban.append(kandidat_pilihan_salah[0]['Indonesia']) # jawaban salah 1
    pilihan_jawaban.append(kandidat_pilihan_salah[1]['Indonesia']) # jawaban salah 2
    random.shuffle(pilihan_jawaban) # acak posisinya
    pilihan = {
        "a" : pilihan_jawaban[0],
        "b" : pilihan_jawaban[1],
        "c" : pilihan_jawaban[2],
    }
    return pilihan

def input_jawaban():
    jawab = False
    while not jawab:
        pilihan = input("Masukkan jawaban anda (a/b/c): ")
        if pilihan.lower() not in ["a","b","c"]:
            print("Pilihan jawaban tidak dikenali")
        else:
            jawab = True
    return pilihan

def mulai_permainan():
    asmaul_husna = load_asmaul_husna()
    jum_pertanyaan = 5
    tampilkan_deksripsi_permainan(jum_pertanyaan)
    benar = 0
    salah = 0
    terpilih = random.sample(asmaul_husna,jum_pertanyaan)
    
    for nama in terpilih:
        pertanyaan = f"Arti dari asmaul husna: {nama["Nama"]} adalah?"
        jawaban_benar = nama["Indonesia"]
        pilihan = siapkan_pilihan(nama,asmaul_husna)
        print(pertanyaan)
        for k in pilihan:
            print(f"{k}. {pilihan[k]}")
        jawaban_user = input_jawaban()
        if pilihan[jawaban_user] == jawaban_benar:
            print("Anda benar!")
            benar += 1
        else:
            salah +=1
            print(f"Salah, jawaban yang benar adalah: {jawaban_benar}")
        
    tampilkan_statistik_permainan(benar,salah)        

mulai_permainan()

