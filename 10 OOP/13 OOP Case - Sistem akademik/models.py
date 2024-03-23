class Mahasiswa:
    def __init__(self,nim,nama,prodi,angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan

class MataKuliah:
    def __init__(self,kode,nama,sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

class Dosen:
    def __init__(self,nidn,nama):
        self.nidn = nidn
        self.nama = nama

class KelasPerkuliahan:
    def __init__(self,kelas,matkul,dosen,ta,semester):
        self.kelas = kelas
        self.matkul = matkul
        self.dosen = dosen
        self.tahun = ta
        self.semester = semester
        self.mahasiswa = []

class MahasiswaKelasPerkuliahan:
    def __init__(self,kelas,mahasiswa):
        self.kelas_perkuliahan = kelas
        self.mahasiswa = mahasiswa

class LogPerkuliahan:
    def __init__(self,kelas,tgl,jam,materi,ruangan,kegiatan):
        self.kelas_perkuliahan = kelas
        self.tgl = tgl
        self.jam = jam
        self.materi = materi
        self.ruangan = ruangan
        self.kegiatan = kegiatan

class KehadiranMahasiswa:
    def __init__(self,log_perkuliahan,mahasiswa):
        self.log_perkuliahan = log_perkuliahan
        self.mahasiswa = mahasiswa
        self.hadir = True

        