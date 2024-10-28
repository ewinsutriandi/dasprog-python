'''
Contoh penggunaan fungsi pada permainan sederhana 1
Game Tebak Angka
'''
import random

def tampilkan_deskripsi_permainan():
    ''' Fungsi untuk menampilkan petunjuk bermain'''
    print("---------------------------------------------------")
    print("GAME TEBAK BILANGAN")
    print("Komputer akan memilih sebuah bilangan secara acak dari 1 s.d 100")
    print("Anda diminta untuk menebak bilangan tersebut")
    input("Tekan ENTER untuk melanjutkan ")
    print("---------------------------------------------------")

def tampilkan_statistik_permainan(menang,kalah):
    print("PERMAINAN BERAKHIR")
    print(f"Total bermain: {menang + kalah}")
    print(f"menang: {menang}, kalah: {kalah}")

def tampilkan_petunjuk_permainan(maks_tebakan):
    print(f"Bilangan rahasia telah dipilih")
    print(f"Anda memiliki {maks_tebakan} kesempatan menebak")
    

def mulai_permainan():
    maks_tebakan = 7
    bil_rahasia = random.randint(1,100)
    jum_tebakan = 0
    tebakan_benar = False
    tampilkan_petunjuk_permainan(maks_tebakan)
    while not tebakan_benar and jum_tebakan < maks_tebakan:
        tebakan = int(input(f"Kesempatan menebak ke-{jum_tebakan+1}. Masukkan tebakan anda: "))
        jum_tebakan += 1
        if tebakan == bil_rahasia:
            tebakan_benar = True
            print(f"Anda berhasil menebak pada tebakan ke {jum_tebakan}")
        else:
            sisa_tebakan = maks_tebakan - jum_tebakan
            if sisa_tebakan > 0:
                if tebakan < bil_rahasia:
                    print("Terlalu kecil",end=". ")
                else:
                    print("Terlalu besar",end=". ")
                print(f"Sisa kesempatan: {sisa_tebakan} kali")
    if tebakan_benar:
        return True
    else:
        print(f"Kesempatan anda habis, bilangan yang benar: {bil_rahasia}")
        return False

def main():
    jum_menang = 0
    jum_kalah = 0
    tampilkan_deskripsi_permainan() # tampilkan petunjuk bermain sebelum permainan dimulai (cukup sekali)
    main_lagi = True
    while main_lagi:
        menang = mulai_permainan()
        if menang:
            jum_menang += 1
        else:
            jum_kalah += 1
        main_lagi = input("Tekan Y kemudian ENTER untuk lanjut bermain, lainnya untuk berhenti ").upper() == "Y"
    tampilkan_statistik_permainan(jum_menang,jum_kalah)

main()