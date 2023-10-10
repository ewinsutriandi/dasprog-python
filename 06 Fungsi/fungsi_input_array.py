l_nilai = [30,70,82,45,80,76,88,54]

# fungsi cari nilai maksimum
def cari_maks(nils):
    maks = 0
    for nilai in l_nilai:
        if nilai > maks:
            maks = nilai
    return maks

print(cari_maks(l_nilai))



