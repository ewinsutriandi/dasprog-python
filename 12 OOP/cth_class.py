'''
Class: sebuah template/blueprint/cetakan 
untuk membuat object
'''

class Persegi:
    # Constructor
    def __init__(self,sisi):
        self.sisi = sisi # sisi adalah atribut object

class PersegiPanjang:
    def __init__(self,pjg,lbr):
        self.pjg = pjg
        self.lbr = lbr

class Mahasiswa:
    def __init__(self,nim,nama,prodi,angkatan):
        self.nim  = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan