class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def keliling(self):
        return 4 * self.sisi
    
    def luas(self):
        return self.sisi * self.sisi
    
class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar

class Lingkaran:
    def __init__(self,jari_jari):
        self.jari_jari = jari_jari
    
    def keliling(self):
        return 3.14 * 2 * self.jari_jari
    
    def luas(self):
        return 3.14 * self.jari_jari * self.jari_jari

# copy paste kode untuk setiap class ke chatGPT, minta chatGPT menjelaskan kode tersebut kemudian memberikan contoh cara penggunaannya