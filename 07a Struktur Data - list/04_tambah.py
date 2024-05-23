# elemen list dapat ditambah menggunakan append dan insert
buah_buahan = ["Apel","Belimbing","Pepaya","Delima","Pisang","Jambu"]
print(buah_buahan) # cetak isi list (kondisi awal)

# Cara 1: Menggunakan append, elemen baru akan diletakkan di akhir list
buah_buahan.append("Manggis") 
print(buah_buahan)

# Cara 2: Menggunakan insert, elemen baru akan disisipkan pada indeks yang diberikan
buah_buahan.insert(2,"Markisa") 
print(buah_buahan)