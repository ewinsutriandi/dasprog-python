# tampilkan pilihan menu aplikasi
# 1. Tambah menu, 2. Catat pesanan 3. Pembayaran

import db
from models import Tamu,Menu,Pesanan

def tampilkan_halaman_utama():
    pilihan = 0
    while pilihan != "4":
        print("PILIH AKSI")
        print("1. Tambah Menu   2. Catat Pesanan Tamu    3.Pembayaran    4. Keluar")
        pilihan = input("Pilih menggunakan angka: ")
        if pilihan == "1":
           tambah_menu()
        elif pilihan == "2":
            catat_pesanan_tamu()
    
def tambah_menu():
    print('TAMBAH MENU BARU')
    nama = input('Nama menu: ')
    jenis = input('Jenis menu 1. Makanan 2. Minuman: ')
    harga = int(input('Harga menu: '))
    if jenis == "1":
        jenis = "Makanan"
    else:
        jenis = "Minuman"
    db.create_menu(nama,jenis,harga)

def catat_pesanan_tamu():
    meja = input("Nomor meja: ")
    pilihan = 0
    daftar_pesanan = []
    while pilihan != "3":
        print('Pilih menu')
        print("1. Menu makanan  2. Menu minuman   3. Selesai")
        pilihan = input("Pilih aksi: ")
        pesanan = None
        if pilihan == "1":
            pesanan = pilih_dari_daftar_menu("Makanan")
        elif pilihan == "2":
            pesanan = pilih_dari_daftar_menu("Minuman")
        if pesanan:
            daftar_pesanan.append(pesanan)
            print(f"{pesanan.jumlah} {pesanan.menu.nama} @ {pesanan.menu.harga}: total {pesanan.total_harga()}")
    print("jumlah pesanan:",len(daftar_pesanan))
    if len(daftar_pesanan) > 0 :
        tamu_id = db.create_tamu(meja)
        for pesanan in daftar_pesanan:
            pesanan.tamu_id = tamu_id
            db.create_pesanan(pesanan) 

def pilih_dari_daftar_menu(tipe):
    daftar_menu = []
    daftar_menu = db.list_menu_by_jenis(tipe)
    print("Pilih berdasarkan ID menu")
    for menu in daftar_menu:
        print(f"Kode {menu.id}: {menu.nama} {menu.harga} ")
    id_menu_terpilih = int(input("Masukkan pilihan: "))
    menu_terpilih = db.menu_by_id(id_menu_terpilih)
    print(menu_terpilih)
    jumlah = int(input("Masukkan jumlah pesanan: "))
    pesanan = Pesanan(menu_terpilih,jumlah)
    return pesanan

tampilkan_halaman_utama()
print("PROGRAM SELESAI")