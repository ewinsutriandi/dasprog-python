'''
Contoh penggunaan fungsi pada permainan sederhana 2
Game Asmaul Husna
'''
import json
import random

def load_asmaul_husna():
    try:
        with open('08 Fungsi/10 asmaul_husna.json') as f:
            d = json.load(f)
            return d["asmaul_husna"]
    except FileNotFoundError:
        print("File tidak ditemukan")

def tampilkan_petunjuk_bermain():
    ''' Fungsi untuk menampilkan petunjuk bermain'''
    print("ARTI ASMAUL HUSNA")
    print("Komputer akan memilih 10 nama dari 99 asmaul husna")
    print("Pilih arti yang benar untuk tiap nama")
    input("Tekan ENTER untuk memulai ")

def tampilkan_statistik_permainan(benar,salah):
    print("PERMAINAN BERAKHIR")
    print(f"Total soal: {benar + salah}")
    print(f"benar: {benar}, salah: {salah}")    

def mulai_permainan():
    data = load_asmaul_husna() 
    pilih_10_nama = random.sample(data,10)
    for nama in pilih_10_nama:
        print(nama['Nama'],nama['Indonesia'])
    

mulai_permainan()

