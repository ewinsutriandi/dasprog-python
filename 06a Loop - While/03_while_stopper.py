'''
While Loop yang berhenti karena dihentikan user
'''
sebuah_kondisi = True

while sebuah_kondisi:
    print("Teks ini akan dicetak berulang selama sebuah_kondisi bernilai True")
    stop = input("Ketik s/S untuk menghentikan perulangan: ")
    if stop.lower() == "s":
        sebuah_kondisi = False

print("perulangan dihentikan")

