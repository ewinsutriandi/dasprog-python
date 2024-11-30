class Siswa:
    def __init__(self,nama,bb,tb):
        self.nama = nama
        self.bb = bb
        self.tb = tb
    
    def bmi(self):
        bmi = self.bb / (self.tb/100) ** 2
        return bmi
    
    def kategori_bmi(self):
        bmi = self.bmi()
        if bmi >= 30:
            return "Obesitas"
        elif bmi >= 25:
            return "Gemuk"
        elif bmi >= 18:
            return "Langsing"
        else:
            return "Kurus"

upin = Siswa("Upin",45,138)
print(upin.kategori_bmi())

# copy paste kode untuk setiap class ke chatGPT, 
# minta chatGPT menjelaskan kode tersebut kemudian memberikan contoh cara penggunaannya