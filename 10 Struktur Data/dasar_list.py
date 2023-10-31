# deklarasi
siswa = ["Upin","Ipin","Jarjit"]
tinggi_siswa = [110,110,112]
berat_siswa = [17,18,19]
# akses, gunakan indeks, mulai dari 0
print(siswa[1]) 
# tambah data
siswa.append("Meilani")
tinggi_siswa.append(114)
berat_siswa.insert(3,20)
print(berat_siswa)
# assignment/update data
siswa[2] = "Ehsan"
print(siswa)
# hapus data
siswa.pop()
print(siswa)
siswa.append("Meilani")
# loop dgn indeks
for i in range(len(siswa)):
    print(siswa[i])

# loop for each
for s in siswa:
    print(s)