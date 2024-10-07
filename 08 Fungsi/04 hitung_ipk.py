# misal, diketahui data nilai kuliah satu semester dalam array
data_nilai = [
    {"matkul": "Dasar Pemrograman", "nilai": "A", "sks": 3},
    {"matkul": "Algoritma Pemrograman", "nilai": "B", "sks": 3},
    {"matkul": "Aljabar linier", "nilai": "A", "sks": 3},
    {"matkul": "Bahasa Indonesia", "nilai": "A", "sks": 2},
    {"matkul": "Bahasa Iggris", "nilai": "A", "sks": 2},
    {"matkul": "Statistik", "nilai": "C", "sks": 2},
]

def hitung_ipk(daftar_nilai_matkul):
    jum_sks = 0 #total jumlah kredit
    jum_nilai = 0 #total nilai
    for nilai_matkul in daftar_nilai_matkul:
            sks = nilai_matkul["sks"]
            grade = nilai_matkul["nilai"]
            bobot = 0
            if grade == "A":
                bobot = 4
            elif grade == "B":
                bobot = 3
            elif grade == "C":
                bobot = 2
            elif grade == "D":
                bobot = 1
            # lakukan akumulasi sks dan nilai
            jum_sks += sks
            jum_nilai += sks * bobot
    
    # hitung ipk
    ipk = jum_nilai / jum_sks
    return ipk

# contoh cara pemakaian
ipk_upin = hitung_ipk(data_nilai)
print(f"{ipk_upin:.2f}")