# list berisi hasil UTS mahasiswa
nilai_uts = [35,65,78,75,22,87,90,32,85,87,65]

# gunakan perulangan for untuk mencari nilai maksimum pada list
maks = nilai_uts[0]

for i in range(1,len(nilai_uts)):
    if nilai_uts[i] > maks:
        maks = nilai_uts[i]

print(f"Nilai UTS tertinggi adalah: {maks}")

