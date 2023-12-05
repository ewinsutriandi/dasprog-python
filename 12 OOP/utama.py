from cth_class import Persegi,PersegiPanjang,Mahasiswa

# p1 dan p2 adalah object Persegi
p1 = Persegi(4)
p2 = Persegi(7)

print(p1.sisi) # akses atribut dengan tanda titik setelah object
print(p2.sisi)

pp1 = PersegiPanjang(3,4)
pp2 = PersegiPanjang(2,3)

print(f"pp1 memiliki pjg {pp1.pjg} dan lebar {pp1.lbr}")

mhs1 = Mahasiswa("12345","Upin","Informatika",2022)

print(f"{mhs1.nama} adalah mahasiswa {mhs1.prodi} angkatan {mhs1.angkatan}")

