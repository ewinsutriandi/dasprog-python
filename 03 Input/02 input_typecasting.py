nama = input("Masukkan nama anda: ")

# typecasating dua baris
angkatan = input("Masukkan angkatan anda: ")
angkatan = int(angkatan)

# typecasating sekaligus dalam satu baris
ipk = float(input("Masukkan IPK anda: "))

print(f"{nama} adalah mahasiswa angkatan {angkatan}")
print(f"{nama} memiliki IPK {ipk}")
