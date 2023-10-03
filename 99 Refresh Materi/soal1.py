'''
Bangun ruang berbentuk bola dengan jari-jari r, 
diketahui memiliki volume sebesar 4/3 πr3 dan luas sebesar 4πr2.
Buatlah sebuah program yang menerima input jari-jari sebuah bola 
dan mencetak volume dan luasnya pada layar. 
Gunakan nilai π = 3.14
'''

jari_jari = input("Masukkan nilai jari-jari: ")
jari_jari = float(jari_jari)

vol = 4/3 * 3.14 * jari_jari ** 3

print(f"Volume bola dengan jari-jari {jari_jari} adalah {vol}")




