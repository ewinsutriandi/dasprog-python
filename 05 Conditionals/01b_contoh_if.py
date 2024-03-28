# Ganti nilai variabel usia dan atau sudah_menikah kemudian amati dampaknya
nama = "Upin"
usia = 17
sudah_menikah = False
bisa_memilih = usia >=17 or sudah_menikah
print(f"{nama} berusia {usia} tahun")
if bisa_memilih:
    print(f"{nama} sudah boleh memilih pada pemilu")