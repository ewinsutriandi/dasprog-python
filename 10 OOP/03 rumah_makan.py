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

nasi_ayam_goreng = Menu("Nasi ayam goreng","makanan",17000)
nasi_ayam_geprek = Menu("Nasi ayam geprek","makanan",21000)
es_teh = Menu("Es teh manis","minuman",4500)
es_kelapa = Menu("Es kelapa muda","minuman",6000)

tamu = Tamu("meja 1")
tamu.pesan(nasi_ayam_goreng,1)
tamu.pesan(nasi_ayam_geprek,2)
tamu.pesan(es_teh,3)
print(tamu)