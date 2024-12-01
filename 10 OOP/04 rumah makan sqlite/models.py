class Menu:
    def __init__(self,nama,jenis,harga,id=0):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
    def __repr__(self):
        return f"{self.nama} @ {self.harga:,.0f}"

class Pesanan:
    def __init__(self,menu,jumlah,tamu_id=0,id=0):
        self.id = id
        self.menu = menu
        self.jumlah = jumlah
        self.tamu_id = tamu_id
        
    def total_harga(self):
        return self.jumlah * self.menu.harga

class Tamu:
    def __init__(self,meja):
        self.id = id
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
        pesanan = f"{len(self.pesanan)} pesanan, total belanja: {self.total_belanja():,.0f}\n"
        if self.sudah_bayar:
            bayar = f"Sudah dibayar"
        else:
            bayar = "Belum dibayar"
        return  meja + pesanan + bayar

