# list berisi hasil UTS mahasiswa
nilai_uts = [35,65,78,75,22,87,90,32,85,87,65]

# gunakan perulangan for untuk mencari nilai minimum pada list

nil_min = nilai_uts[0]
for nil in nilai_uts:
    if nil < nil_min:
        nil_min = nil
print(nil_min) 