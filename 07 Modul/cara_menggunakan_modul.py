import bangun_datar # cara 1
print(bangun_datar.luas_persegi(3))

import bangun_datar as bd # cara 2
print(bd.luas_persegi_panjang(3,4))

from bangun_datar import luas_segitiga # cara 3
print(luas_segitiga(4,5))

from bangun_datar import luas_trapesium,luas_lingkaran
print(luas_lingkaran(6))
print(luas_trapesium(3,4,5))

from bangun_datar import luas_persegi as lp # cara 4
print(lp(6))

