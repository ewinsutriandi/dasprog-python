"""
Suhu dalam skala Fahrenheit (°F) dapat dikonversi ke dalam skala Celcius (°C) dengan rumus:

C = (F - 32) * 5 / 9

Dimana:
C, suhu dalam skala Celcius
F, suhu dalam skala Fahrenheit

Buatlah fungsi yang melakukan konversi suhu dari skala Fahrenheit ke skala Celcius.

Buatlah program yang menerima input suhu dalam skala fahrenheit, kemudian memanggil fungsi konversi tersebut untuk mencetak suhu yang sama dalam skala Celcius.

"""

def fahrenheit_ke_celcius(suhu_f):
    c = (suhu_f-32) * 5 /9
    return c

suhu = float(input("Masukkan suhu dalam skala fahrenheit: "))
suhu_c = fahrenheit_ke_celcius(suhu)
print(f"{suhu}°F setara dengan {suhu_c}°C ")