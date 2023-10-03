'''
Body Mass Index (indeks massa tubuh), atau BMI dihitung dengan rumus sebagai berikut.
BMI = bb / tb2 
bb: berat badan dalam satuan kilogram
tb: tinggi badan dalam satuan meter
Buatlah sebuah program yang menerima input nama, 
tinggi badan dalam satuan cm, dan berat badan seseorang dalam satuan kg, 
kemudian menghitung BMI dan mencetak nilainya ke layar.
Catatan: 1 meter = 100 cm
'''

bb = int(input("Masukkan berat badan (kg): "))
tb = int(input("Masukkan tinggi badan (cm): "))

tb_m = tb / 100

bmi = bb / (tb_m ** 2)

print(f"BMI = {bmi}")

if bmi < 17:
    print("Tergolong kurus")
elif bmi < 25:
    print("Tergolong normal")
elif bmi < 30:
    print("Tergolong gemuk")
else:
    print("Tergolong obesitas")



