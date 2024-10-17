import requests

def get_data_kurs():
    url = "https://api.exchangerate-api.com/v4/latest/IDR"
    rslt = requests.get(url)
    if rslt.status_code == requests.codes.ok:
        return rslt.json()
    else:
        return False

def nilai_tukar_idr(jum,mata_uang):
    kurs = get_data_kurs()
    nilai_idr = None
    if kurs and mata_uang in kurs["rates"]:
        x_rate = kurs["rates"][mata_uang]
        nilai_idr = jum * 1 / x_rate
    return nilai_idr

jum_uang = float(input("Masukkan jumlah uang: "))
mata_uang = input("Masukkan mata uang: ").upper()
data = nilai_tukar_idr(jum_uang,mata_uang)
if data:
    print(data)
else:
    print("data tidak ditemukan")