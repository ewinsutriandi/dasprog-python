# list berisi hasil UTS mahasiswa
nilai_uts = [35,65,78,75,22,87,90,32,85,87,65]

# gunakan perulangan for untuk mencari nilai maksimum pada list
sum = 0

for nil in nilai_uts:
    sum += nil
rerata = sum / len(nilai_uts)
print(f"Nilai rata-rata UTS adalah: {rerata}")

