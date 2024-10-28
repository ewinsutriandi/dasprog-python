import requests

def get_data_kurs():
    '''
    Mengambil data nilai tukar rupiah dari web API yg menyediakan nilai tukar
    '''
    url = "https://api.exchangerate-api.com/v4/latest/IDR" # API untuk nilai tukar rupiah
    rslt = requests.get(url)
    if rslt.status_code == requests.codes.ok:
        return rslt.json()
    else:
        return False

def nilai_tukar_idr(kurs,jum,mata_uang):
    '''
    Melakukan kalkulasi nilai tukar jumlah dan mata uang tertentu ke rupiah
    '''
    nilai_idr = None
    if kurs and mata_uang in kurs["rates"]:
        x_rate = kurs["rates"][mata_uang]
        nilai_idr = jum * 1 / x_rate
    return nilai_idr

kurs = get_data_kurs()
lagi = "Y"
while lagi.upper() == "Y":
    jum_uang = float(input("Masukkan jumlah uang: "))
    mata_uang = input("Masukkan jenis mata uang (cth:EUR): ").upper()
    nilai_tukar = nilai_tukar_idr(kurs,jum_uang,mata_uang)
    if nilai_tukar:
        print(f"Nilai {jum_uang:,.2f} {mata_uang} = {nilai_tukar:,.2f} IDR")
    else:
        print("data tidak ditemukan")
    lagi = input("Tekan Y/y kemudian ENTER untuk mata uang lainnya: ")

print("Program selesai")