nama = input("Masukkan nama anda: ")
thn_lulus = input("Anda lulus tahun: ")
tipe_sekolah = input("SMA/SMK: ")
jurusan = ""
bhs_pemrograman = ""

if tipe_sekolah == "SMK":
    jurusan = input("Jurusan anda: ")
    if jurusan == "TKJ" or jurusan == "RPL":
        bhs_pemrograman = input("Bahasa pemrograman yang pernah dipelajari: ")

print(f"{nama} lulus tahun {thn_lulus} dari {tipe_sekolah}")
if tipe_sekolah == "SMK":
    print(f"{nama} dulu bersekolah di SMK jurusan {jurusan}")
    if bhs_pemrograman != "":
        print(f"{nama} pernah belajar bahasa pemrograman {bhs_pemrograman}")

