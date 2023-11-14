'''
Bangun ruang berbentuk bola dengan jari-jari r, 
diketahui memiliki volume sebesar 4/3 πr3 dan luas sebesar 4πr2.
Buatlah sebuah program yang menerima input jari-jari sebuah bola 
dan mencetak volume dan luasnya pada layar. 
Gunakan nilai π = 3.14
'''

jari_jari = float(input("Masukkan jari-jari: "))
vol = (4/3) * 3.14 * jari_jari ** 3
luas = 4 * 3.14 * jari_jari ** 2

print("Volume bola: ", vol)
print("Luas bola: ", luas)

