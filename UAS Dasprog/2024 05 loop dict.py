'''
Body Mass Index (indeks massa tubuh), atau BMI dihitung dengan rumus sebagai berikut.
BMI = bb / tb2
dimana,
bb: berat badan dalam satuan kilogram
tb: tinggi badan dalam satuan meter

Berikut adalah tabel berisi beberapa orang beserta jenis kelamin, berat badan, dan tinggi badannya. Buatlah program untuk menentukan:
Siswa dengan BMI terbesar
Siswa dengan BMI terkecil
Rata-rata BMI siswa laki-laki

'''

daftar_siswa = [
    {'nama': 'Dinara Kamelia', 'jenis_kelamin': 'P', 'berat': 55, 'tinggi': 161},
    {'nama': 'Rustam Perkasa', 'jenis_kelamin': 'L', 'berat': 69, 'tinggi': 174},
    {'nama': 'Ridwan Ali', 'jenis_kelamin': 'L', 'berat': 60, 'tinggi': 169},
    {'nama': 'Ricardo Salami', 'jenis_kelamin': 'L', 'berat': 79, 'tinggi': 170},
    {'nama': 'Ningsih Ayu', 'jenis_kelamin': 'P', 'berat': 58, 'tinggi': 163},
    {'nama': 'Laetisia Cantika', 'jenis_kelamin': 'P', 'berat': 49, 'tinggi': 158},
    {'nama': 'Roronoa Zoro', 'jenis_kelamin': 'L', 'berat': 85, 'tinggi': 181}
]


bmi_terbesar = daftar_siswa[0]
bmi_terkecil = daftar_siswa[0]
jum_siswa_l = 0
tot_bmi_siswa_l = 0
for data in daftar_siswa:
    bmi = data["berat"] / (data["tinggi"]/100)**2
    data["bmi"] = bmi
    # cari BMI terbesar dan terkecil
    if data["bmi"] > bmi_terbesar["bmi"]:
        bmi_terbesar = data
    elif data["bmi"] < bmi_terkecil["bmi"]:
        bmi_terkecil = data
    # cari rerata BMI siswa laki-laki
    if data["jenis_kelamin"] == "L":
        jum_siswa_l += 1
        tot_bmi_siswa_l += bmi

rerata_bmi_l = tot_bmi_siswa_l/jum_siswa_l
print(f"Siswa dengan BMI terbesar adalah {bmi_terbesar['nama']} dengan BMI {bmi_terbesar['bmi']}")
print(f"Siswa dengan BMI terkecil adalah {bmi_terkecil['nama']} dengan BMI {bmi_terkecil['bmi']}")
print(f"Rata-rata BMI siswa laki-laki: {rerata_bmi_l:0.2f}")