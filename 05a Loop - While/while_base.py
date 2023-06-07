sebuah_kondisi = True

while sebuah_kondisi: # infinite loop
    print("Sebuah kondisi bernilai", sebuah_kondisi)
    berhenti = input("Berhenti? (y)")
    if berhenti == 'y':
        sebuah_kondisi = False
