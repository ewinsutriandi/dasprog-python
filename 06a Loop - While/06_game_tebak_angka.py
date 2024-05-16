import random

bil = random.randint(1,100) # menghasilkan bil acak pd rentang 1 s.d 100
tebakan_benar = False
tebakan_maks = 7
jum_tebakan = 0

print("Komputer telah memilih sebuah bilangan secara acak dari 1 s.d 100")

while not tebakan_benar and jum_tebakan < tebakan_maks:
    jum_tebakan = jum_tebakan + 1
    print(f"Ini adalah tebakan ke-{jum_tebakan} anda")
    tebakan = int(input("Masukkan tebakan anda: "))
    if bil == tebakan:
        tebakan_benar = True
    elif bil > tebakan:
        print("Tebakan anda kekecilan")
    else:
        print("Tebakan anda kebesaran")

if tebakan_benar:
    print(f"Selamat tebakan anda benar")
else:
    print(f"Tebakan anda salah, bilangan yang benar {bil}")