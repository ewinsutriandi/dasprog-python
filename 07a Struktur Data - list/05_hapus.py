# elemen list dapat dihapus dengan menggunakan remove, del, dan pop
buah_buahan = ["Apel","Belimbing","Pepaya","Delima","Pisang","Jambu"]
print(buah_buahan) # cetak isi list (kondisi awal)

# menghapus menggunakan remove
buah_buahan.remove("Belimbing") # Buang belimbing dari list
print(buah_buahan) 

# menghapus menggunakan del
del buah_buahan[2] # Buang elemen pada indeks-2
print(buah_buahan) 

# menghapus menggunakan pop
buang = buah_buahan.pop(1) # Buang elemen pada indeks-1, cara ini menghasilkan return value berupa elemen yang dibuang
print(buah_buahan) 
print(buang)