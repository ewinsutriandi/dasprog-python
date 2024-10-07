
def hitung_nilai_akhir(n_hdr,n_partisipasi,n_tgs,n_uts,n_uas):
    '''Fungsi untuk menghitung nilai akhir berdasarkan nilai komponen penyusunnya'''
    # bobot masing-masing komponen
    b_hdr = 0.15
    b_part= 0.15
    b_tgs = 0.2
    b_uts = 0.25
    b_uas = 0.25

    # kalkulasi n_akhir
    n_akhir = b_hdr * n_hdr + b_part * n_partisipasi + b_tgs * n_tgs + b_uts * n_uts + b_uas * n_uas
    return n_akhir # return value

# Contoh cara menggunakan
na_upin = hitung_nilai_akhir(80,70,86,60,75)
na_ipin = hitung_nilai_akhir(90,80,86,87,84)

print(f"Nilai akhir upin adalah: {na_upin:.2f}")
print(f"Nilai akhir ipin adalah: {na_ipin:.2f}")

