'''
Berikut adalah aturan pemberian donor darah berdasarkan golongan darahnya
Orang bergolongan darah O hanya boleh menerima dari donor bergolongan darah O.
Orang bergolongan darah A boleh menerima dari donor bergolongan darah O dan A.
Orang bergolongan darah B boleh menerima dari donor bergolongan darah O dan B.
Orang bergolongan darah AB boleh menerima dari donor golongan darah apapun.
Buat sebuah fungsi yang menerima input parameter berupa golongan darah pendonor dan golongan darah penerima kemudian mengembalikan nilai True bila donor sesuai, dan False bila sebaliknya.
'''

def cocok_donor(golongan_darah_pendonor, golongan_darah_penerima):
    if golongan_darah_pendonor == "O":
        return True
    if golongan_darah_penerima == "AB":
        return True
    if golongan_darah_pendonor == "A":
        return golongan_darah_penerima == "A"
    if golongan_darah_pendonor == "B":
        return golongan_darah_penerima == "B"
    return False


golongan_donor = input("Masukkan golongan darah pendonor: ")
golongan_penerima =input("Masukkan golongan darah penerima: ")
hasil_cocok = cocok_donor(golongan_donor, golongan_penerima)
print(hasil_cocok)