import random

def tampilkan_petunjuk_bermain():
    ''' Fungsi untuk menampilkan petunjuk bermain'''
    print("GAME TEBAK BILANGAN")
    print("Komputer akan memilih sebuah bilangan secara acak dari 1 s.d 100")
    print("Anda diminta untuk menebak bilangan tersebut")
    input("Tekan ENTER untuk melanjutkan ")

def tampilkan_statistik_permainan(menang,kalah):
    print("PERMAINAN BERAKHIR")
    print(f"Total bermain: {menang + kalah}")
    print(f"menang: {menang}, kalah: {kalah}")

def mulai_permainan():
    maks_tebakan = 7
    bil_rahasia = 0
    jum_tebakan = 0
    bil_rahasia = random.randint(1,100)
    jum_tebakan = 0
    tebakan_benar = False
    print("---------------------------------------------------")
    print(f"Komputer telah memilih sebuah bilangan rahasia")
    print(f"Anda mendapatkan {maks_tebakan} kesempatan menebak")
    print("---------------------------------------------------")
    while not tebakan_benar and jum_tebakan <= maks_tebakan:
        tebakan = int(input(f"Kesempatan menebak ke-{jum_tebakan+1}. Masukkan tebakan anda: "))
        jum_tebakan += 1
        if tebakan == bil_rahasia:
            tebakan_benar = True
            print(f"Anda berhasil menebak pada tebakan ke {jum_tebakan}")
        else:
            if tebakan < bil_rahasia:
                print("Tebakan anda terlalu kecil")
            else:
                print("Tebakan anda terlalu besar")
    if tebakan_benar:
        return True
    else:
        print(f"Anda gagal menebak, bilangan yang benar: {bil_rahasia}")
        return False

def main():
    menang = 0
    kalah = 0
    tampilkan_petunjuk_bermain() # tampilkan petunjuk bermain sebelum permainan dimulai (cukup sekali)
    main_lagi = True
    while main_lagi:
        menang = mulai_permainan()
        if menang:
            menang += 1
        else:
            kalah += 1
        main_lagi = input("Tekan Y kemudian ENTER untuk lanjut bermain, lainnya untuk berhenti ").upper() == "Y"
    tampilkan_statistik_permainan(menang,kalah)
main()