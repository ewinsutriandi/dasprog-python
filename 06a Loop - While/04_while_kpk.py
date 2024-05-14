'''
Buatlah program yang menerima dua buah bilangan bulat
kemudian menghitung dan mencetak KPKnya
'''

b1 = int(input("Bil 1: "))
b2 = int(input("Bil 2: "))

calon_kpk = b1
kpk_ketemu = False

while not kpk_ketemu:
    if calon_kpk % b2 == 0:
        kpk_ketemu = True
    else:
        calon_kpk = calon_kpk + b1

print(f"{b1} dan {b2} memiliki KPK {calon_kpk}")