nilai_berhitung = [["Upin",80,90],["Jarjit",70,75],["Ipin",94,90],["Mail",88,96],["Ehsan",92,75]]

print(nilai_berhitung[1][2])

# buat fungsi untuk mencari siswa TK Tadika Mesra dengan nilai berhitung paling tinggi
# nilai berhitung dihitung dari rata-rata dua ujian 

def cari_maks(l_nilai):
    nilai_maks = 0
    siswa_mks = ''
    for nil_siswa in l_nilai:
        siswa = nil_siswa[0]
        nilai = (nil_siswa[1] + nil_siswa[2])/2
        if nilai > nilai_maks:
            nilai_maks = nilai
            siswa_mks = siswa
    
    return [siswa_mks,nilai_maks]

print(cari_maks(nilai_berhitung))

