# https://koding.alza.web.id/menggunakan-modul-datetime/
import datetime

tanggal_saat_ini = datetime.date.today() 
print(tanggal_saat_ini) # tanggal pada hari ini akan ditampilkan di layar

saat_ini = datetime.datetime.now() 
print(saat_ini) # waktu saat ini akan ditampilkan di layar

# mengisi variabel dengan tanggal tertentu
tgl = datetime.date(2019, 7, 31) # tahun, bulan, tanggal
print(tgl)

# mengakses nilai pada variabel
print("Tahun:", tgl.year)
print("Bulan:", tgl.month)
print("Tanggal:", tgl.day)

# dst, lihat referensi di atas halaman