# deklarasi, list dideklarasikan dengan menggunakan kurung siku [ ]
# setiap elemen pada list dipisah menggunakan tanda koma ,
kec_lotim = ["Selong","Masbagik","Labuhan Haji","Sikur","Suralaga","Sukamulia"]
wisata_lotim = ["Pantai Tg. Luar", "Pantai Pink", "Lemor", "Sembalun", "Gili Lampu", "Aik Nyet"]
print(wisata_lotim)
print(kec_lotim)

# mengakses elemen menggunakan indeks (nomor urut), yang dimulai dari 0
print(kec_lotim[2])
print(wisata_lotim[4])

# mengganti elemen/update
kec_lotim[3] = "Pringgabaya"
print(kec_lotim)

# menambah elemen dengan append
kec_lotim.append("Sikur")
wisata_lotim.append("Pantai Ketapang")
print(kec_lotim)
print(wisata_lotim)

# menambah elemen dengan insert
kec_lotim.insert(2,"Sakra")
wisata_lotim.insert(3,"Joben")
print(kec_lotim)
print(wisata_lotim)

# menghapus elemen dengan pop()
kec_lotim.pop()
wisata_lotim.pop()
print(kec_lotim)
print(wisata_lotim)

# menghapus elemen dengan pop(nomor_urut)
kec_lotim.pop(3)
wisata_lotim.pop(2)
print(kec_lotim)
print(wisata_lotim)

# menghapus elemen dengan remove
kec_lotim.remove("Selong")
wisata_lotim.remove("Aik Nyet")
print(kec_lotim)
print(wisata_lotim)

# mendapatkan jumlah elemen pada list dengan len()
print(len(kec_lotim))
print(len(wisata_lotim))

# mendapatkan index sebuah elemen pada list
print(kec_lotim.index("Sakra"))
print(wisata_lotim.index("Joben"))

# perulangan for pada list
for kc in kec_lotim:
    print(kc)

for dw in wisata_lotim:
    print(dw)

# mengosongkan list dengan clear
kec_lotim.clear()
print(kec_lotim)