# input data
nama = input("Nama: ")
bb = int(input("Berat badan: "))
tb = int(input("Tinggi badan: "))

# kalkulasi BMI
tb_m = tb /100
bmi = bb / tb_m ** 2

# klasifikasi
if bmi < 17.5:
    tipe = "kurus"
elif bmi < 23:
    tipe = "normal"
elif bmi < 28:
    tipe = "gemuk"
else:
    tipe = "obesitas"

# cetak
print(f"{nama} memiliki bmi {bmi}, tergolong {tipe}")