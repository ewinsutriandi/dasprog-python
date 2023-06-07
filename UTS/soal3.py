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

nama = input("Masukkan nama: ")
tb = int(input("Tinggi badan (cm): "))
bb = int(input("Berat badan (kg): "))
tb_meter = tb / 100
bmi = bb / tb_meter ** 2

print(f"{nama} memiliki BMI {bmi}")



