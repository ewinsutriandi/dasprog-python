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
        elif pilihan == "3":
            catat_pembayaran()
    
def tambah_menu():
    print('TAMBAH MENU BARU')
    nama = input('Nama menu: ')
    jenis = input('Jenis menu 1. Makanan 2. Minuman: ')
    harga = int(input('Harga menu: '))
    if jenis == "1":
        jenis = "Makanan"
    else:
        jenis = "Minuman"
    menu = Menu(nama,jenis,harga)
    db.create_menu(menu)

def catat_pesanan_tamu():
    meja = input("Nomor meja: ")
    tamu = Tamu(meja)
    pilihan = 0
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
            tamu.pesan(pesanan)
            print(f"{pesanan.jumlah} {pesanan.menu.nama} @ {pesanan.menu.harga}: total {pesanan.total_harga()}")
    print("jumlah pesanan:",len(tamu.pesanan))
    db.create_tamu(tamu)

def pilih_dari_daftar_menu(tipe):
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

def catat_pembayaran():
    daftar_tamu = []
    daftar_tamu = db.list_tamu_belum_bayar()
    if len(daftar_tamu) > 0:
        for tamu in daftar_tamu:
            print(f"ID {tamu.id} pada meja {tamu.meja}")
        tamu_id = int(input("Masukkan ID tamu: "))
        tamu = db.tamu_by_id(tamu_id)
        tampilkan_daftar_pesanan(tamu)
        print('Pilih menu')
        print("1. Update status bayar  2. Batal  ")
        respon = input("Masukkan pilihan: ")
        if respon == "1":
            db.update_status_bayar(tamu_id)
            print("Status pembayaran sudah diupdate")
        else:
            print("Pembayaran dibatalkan")
    else:
        print("Semua tamu sudah membayar")

def tampilkan_daftar_pesanan(tamu):
    print(f"Daftar pesanan tamu pada meja {tamu.meja}:")
    daftar_pesanan = db.list_pesanan_by_tamu_id(tamu.id)
    if len(daftar_pesanan) > 0:
        total_bayar = 0
        for pesanan in daftar_pesanan:
            print(f"{pesanan.jumlah} {pesanan.menu.nama} @ {pesanan.menu.harga:,.0f} total {pesanan.total_harga():,.0f}" )
            total_bayar += pesanan.total_harga()
        print(f"TOTAL YG HARUS DIBAYAR: {total_bayar:,.0f}")
    else:
        print("Tamu belum memiliki pesanan")

tampilkan_halaman_utama()
print("PROGRAM SELESAI")