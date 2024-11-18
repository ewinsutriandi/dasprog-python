class Menu:
    def __init__(self,nama,jenis,harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
    def __repr__(self):
        return f"{self.nama} seharga {self.harga}"
class Pesanan:
    def __init__(self,menu,jumlah):
        self.menu = menu
        self.jumlah = jumlah
    
    def total_harga(self):
        return self.jumlah * self.menu.harga

class Tamu:
    def __init__(self,meja):
        self.meja = meja
        self.sudah_bayar = False
        self.pesanan = []
    
    def pesan(self,menu,jumlah):
        pesanan_baru = Pesanan(menu,jumlah)
        self.pesanan.append(pesanan_baru)

    def total_belanja(self):
        total = 0
        for p in self.pesanan:
            total += p.total_harga()
        return total
    
    def bayar(self):
        self.sudah_bayar = True

    def __repr__(self):
        meja = f"Pelanggan pada meja {self.meja} \n"
        pesanan = f"{len(self.pesanan)} pesanan, total belanja: {self.total_belanja()}\n"
        if self.sudah_bayar:
            bayar = f"Sudah dibayar"
        else:
            bayar = "Belum dibayar"
        return  meja + pesanan + bayar

# Load Menu
import json
def load_menu():
    daftar_menu = []
    with open("10 OOP/03 menu_rumah_makan.json") as f:
        json_menu =  json.load(f) 
        for menu in json_menu:
            m = Menu(menu["nama"],menu["jenis"],menu["harga"])
            daftar_menu.append(m)
    return daftar_menu

menu = load_menu()
print(menu)