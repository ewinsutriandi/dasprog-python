# Operator logika: and, or, not

# OR, bernilai True jika minimal salah satu operand True
nama = "Upin"
thn_lahir = 2014
usia = 2023 - thn_lahir
sdh_nikah = True
blh_memilih = (usia >= 17) or sdh_nikah

print(f"{nama} boleh memilih: {blh_memilih}")

# AND, bernilai True jika kedua operand True
cukup_umur = True
waras = True
wjb_shlt = cukup_umur and waras

print(f"{nama} wajib sholat: {wjb_shlt}")

# NOT, kebalikan/invers dari nilai logika
print(f"{nama} tidak wajib sholat: {not wjb_shlt}")



