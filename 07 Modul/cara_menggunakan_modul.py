import bangun_datar  # cara 1
print(bangun_datar.luas_persegi(3))
print(bangun_datar.luas_persegi_panjang(3,4))

import bangun_datar as bd # cara 2
print(bd.luas_segitiga(4,8))

from bangun_datar import luas_persegi # cara 3
print(luas_persegi(7))

from bangun_datar import luas_segitiga as l_sgtg # cara 4
print(l_sgtg(6,5))

from bangun_datar import luas_persegi,luas_persegi_panjang # cara 5
print(luas_persegi(5))
print(luas_persegi_panjang(7,8))

