import datetime
class Menu:
    def __init__(self,nama,jenis,harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
    
class Pesanan:
    def __init__(self,menu,jumlah):
        self.menu = menu
        self.jumlah = jumlah
        self.waktu_pesan = datetime.datetime.now()
    
    def total_harga(self):
        return self.jumlah * self.menu.harga

class Tamu:
    def __init__(self,meja):
        self.meja = meja
        self.datang = datetime.datetime.now()
        self.cara_bayar = None
        self.waktu_bayar = None
        self.pesanan = []
    
    def pesan(self,menu,jumlah):
        pesanan_baru = Pesanan(menu,jumlah)
        self.pesanan.append(pesanan_baru)

    def total_belanja(self):
        total = 0
        for p in self.pesanan:
            total += p.total_harga()
        return total
    
    def bayar(self,cara):
        self.waktu_bayar = datetime.datetime.now()
        self.cara_bayar = cara

    def __repr__(self):
        datang = f"Pelanggan pada {self.meja}, datang {self.datang} \n"
        pesanan = f"{len(self.pesanan)} pesanan, total belanja: {self.total_belanja()}\n"
        if self.cara_bayar != None:
            bayar = f"Pembayaran pada {self.waktu_bayar}, {self.cara_bayar}"
        else:
            bayar = "Belum dibayar"
        return  datang + pesanan + bayar