# perulangan pada list


# Cara 1: Menggunakan indeks dengan while dan len
buah_buahan = ["Apel","Belimbing","Pepaya","Delima","Pisang","Jambu"]
i = 0
while i < len(buah_buahan):
    print(buah_buahan[i])
    i+=1
print()

# Cara 1: Menggunakan indeks dengan for-range dan len
buah_buahan = ["Apel","Belimbing","Pepaya","Delima","Pisang","Jambu"]
for i in range(len(buah_buahan)):
    print(buah_buahan[i])
print()

# Cara 3: Menggunakan for each
for buah in buah_buahan:
    print(buah)




