'''
Body Mass Index (indeks massa tubuh), atau BMI dihitung dengan rumus sebagai berikut.
BMI = bb / tb2 
bb: berat badan dalam satuan kilogram
tb: tinggi badan dalam satuan meter
Buatlah sebuah program yang menerima input nama, 
tinggi badan dalam satuan cm, dan berat badan seseorang dalam satuan kg.
Hitung BMI dan klasifikasikan jenis badan orang dimaksud,
dimana
< 17 kurus
17 s.d 25 normal
25 s.d 30 gemuk
>30 obesitas
Catatan: 1 meter = 100 cm

Gunakan fungsi dalam menyelesaikan soal di atas
'''

def htg_bmi(bb,tb): 
    tb = tb /100
    bmi = bb / (tb ** 2)
    return bmi

def kateg_bmi(bmi):
    jenis_badan = "obesitas"
    if bmi < 17:
        jenis_badan = "kurus"
    elif bmi < 25:
        jenis_badan = "normal"
    elif bmi < 30:
        jenis_badan = "gemuk"
    return jenis_badan

bb = int(input("Berat badan?: "))
tb = int(input("Tinggi badan?: "))

bmi = htg_bmi(bb,tb)
jenis_badan = kateg_bmi(bmi)

print(f" BMI: {bmi}, jenis {jenis_badan}")
