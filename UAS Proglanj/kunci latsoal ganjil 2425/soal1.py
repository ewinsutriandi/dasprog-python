"""
Sebuah persegi panjang dengan panjang 6 dan lebar 4 memiliki luas 24 (panjang x lebar) dan keliling 20 (2 x panjang + 2 x lebar)
Dari deskripsi tersebut buatlah class persegi panjang yang dan object yang merepresentasikan persegi panjang dimaksud

"""
class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar

pp1 = PersegiPanjang(6,4)
