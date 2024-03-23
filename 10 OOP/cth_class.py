'''
Class: sebuah template/blueprint/cetakan 
untuk membuat object
'''
import datetime

class Persegi:
    # Constructor
    def __init__(self,sisi):
        self.sisi = sisi # sisi adalah atribut object
    
    def keliling(self):
        return 4 * self.sisi

    def luas(self):
        return self.sisi ** 2

class PersegiPanjang:
    def __init__(self,pjg,lbr):
        self.pjg = pjg
        self.lbr = lbr
    
    def keliling(self):
        return 2 * (self.pjg + self.lbr)

    def luas(self):
        return self.pjg * self.lbr

class Mahasiswa:
    def __init__(self,nim,nama,prodi,angkatan):
        self.nim  = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
    
    def semester(self):
        tahun = datetime.date.today().year
        bulan = datetime.date.today().month
        selisih_tahun = tahun - self.angkatan
        semester = selisih_tahun * 2
        if bulan < 8:
            semester -= 1
        else:
            semester += 1
        return semester