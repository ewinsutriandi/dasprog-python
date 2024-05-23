'''
Buatlah program yang menerima sebuah bilangan bulat
kemudian mencari seluruh faktor dari bilangan tersebut
dan mencetaknya ke layar
'''

bil = int(input("Masukkan sebuah bilangan bulat: "))
faktor = []
for i in range(1,bil+1):
    if bil % i == 0:
        faktor.append(i)

print(f"faktor dari {bil} adalah: {faktor}")