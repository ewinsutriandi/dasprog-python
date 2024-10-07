
def hitung_nilai_akhir(n_hdr,n_partisipasi,n_tgs,n_uts,n_uas):
    '''Fungsi untuk menghitung nilai akhir berdasarkan nilai komponen penyusunnya'''
    # bobot masing-masing komponen nilai
    b_hdr = 0.15
    b_part= 0.15
    b_tgs = 0.2
    b_uts = 0.25
    b_uas = 0.25

    # kalkulasi n_akhir
    n_akhir = b_hdr * n_hdr + b_part * n_partisipasi + b_tgs * n_tgs + b_uts * n_uts + b_uas * n_uas
    return n_akhir # return value

def grade(n_akhir):
    '''Fungsi untuk konversi nilai akhir menjadi grade'''
    grade = "E"
    if n_akhir >= 85:
        grade = "A"
    elif n_akhir >= 70:
        grade = "B"
    elif n_akhir >= 55:
        grade = "C"
    elif n_akhir >= 40:
        grade = "D"
    return grade

# Contoh cara menggunakan 1
na_upin = hitung_nilai_akhir(80,70,86,60,75)
grade_upin = grade(na_upin)

# Contoh cara menggunakan 2
grade_ipin = grade(hitung_nilai_akhir(90,80,86,87,84))

print(f"Upin mendapatkan nilai: {grade_upin}")
print(f"Ipin mendapatkan nilai: {grade_ipin}")

