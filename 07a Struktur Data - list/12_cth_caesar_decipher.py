# Contoh enkripsi sederhana dengan Caesar Cipher
# Decipher (menerjemahkan) teks yang telah dienkripsi sebelumnya
abjad = ['a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z']
cipher = 2
teks = "kphqtocvkmc wpkxgtukvcu jcobcpycfk"
hasil_enkripsi = ""
for t in teks:
    if t != " ":
        indeks_lama = abjad.index(t)    
        indeks_baru = (indeks_lama - cipher) % len(abjad)
        hasil_enkripsi = hasil_enkripsi + abjad[indeks_baru]
    else:
        hasil_enkripsi = hasil_enkripsi + " "

print(hasil_enkripsi)


