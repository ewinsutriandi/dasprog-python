# https://koding.alza.web.id/menggunakan-modul-random-dari-standard-library/
import random as rnd

# Menghasilkan bil. acak pada rentang 1 s.d 100
bil_acak = rnd.randint(1,100)
print(bil_acak)

# Mensimulasikan lemparan dadu
dadu_1 = rnd.randint(1,6)
print(dadu_1)

# Memilih sebuah elemen dari list
l_siswa = ["Upin","Ipin","Mail","Meimei","Jarjit","Devi","Susanti","Ehsan"]
siswa_terpilih = rnd.choice(l_siswa)
print(siswa_terpilih)

# Memilih beberapa elemen sekaligus
siswa_terpilih = rnd.sample(l_siswa,k=3)
print(siswa_terpilih)

# Mengacak urutan
rnd.shuffle(l_siswa)
print(l_siswa)

