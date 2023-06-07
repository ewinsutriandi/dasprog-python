nilai_akhir = input("Nilai akhir anda: ")
nilai_akhir = float(nilai_akhir)

grade = "E"

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
elif nilai_akhir >= 40:
    grade = "D"

print(f"Nilai anda: {nilai_akhir}")
print(f"Anda mendapatkan grade {grade}")


