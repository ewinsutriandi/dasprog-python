bil = input("Masukkan sebuah bilangan: ")
bil = int(bil)

print(f"Anda memasukkan bilangan {bil}")

if bil > 10:
    print(f"{bil} lebih besar dari 10")
elif bil < 10:
    print(f"{bil} lebih kecil dari 10")
else:
    print(f"Bilangan yang anda masukkan sama dengan 10")


