'''
While Loop yang berhenti karena dihentikan user
'''
sebuah_kondisi = True

while sebuah_kondisi:
    print("Hello, world!")
    stop = input("Ketik s untuk berhenti: ")
    if stop == "s":
        sebuah_kondisi = False



