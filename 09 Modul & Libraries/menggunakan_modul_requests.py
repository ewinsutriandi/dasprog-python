import requests

api_url = 'https://api.exchangerate-api.com/v4/latest/IDR' # alamat API
rslt = requests.get(api_url) # mengirimkan request ke alamat API

print(rslt)

if rslt.status_code == requests.codes.ok : # server memberikan respon ok
  hasil = rslt.json() # konversi hasil dari format json ke dictionary
  nilai_tukar_all = hasil['rates'] # ambil rate konversi tiap mata uang ke IDR
  mata_uang_l = ["USD","GBP","JPY","IRR","VND","THB"]
  for mata_uang in mata_uang_l:
    nilai_1IDR = nilai_tukar_all[mata_uang]
    nilai_keIDR = 1 /nilai_1IDR
    print(f"Nilai tukar 1 {mata_uang} adalah {nilai_keIDR:.2f} IDR")
else :
  print('Gagal mendapatkan respon yang diinginkan dari server')

  