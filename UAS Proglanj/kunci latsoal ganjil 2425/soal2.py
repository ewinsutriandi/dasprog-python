"""
Seorang mahasiswa dengan nama Upin bin Amaq Ros adalah mahasiswa pada prodi Sistem Informasi angkatan 2023 dengan NIM 19523081
Dari deskripsi tersebut buatlah class Mahasiswa yang dan object yang merepresentasikan mahasiswa dimaksud
"""

class Mahasiswa:
    def __init__(self,nim,nama,prodi,angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan
    
mhs1 = Mahasiswa("19523081","Upin bin Amaq Ros","Sistem Informasi",2023)