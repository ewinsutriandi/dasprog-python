import json

def load_data(): 
    try:
        with open('08 Fungsi/04 nilai_matkul.json') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File tidak ditemukan")
        return None
    except json.JSONDecodeError:
        print("File JSON tidak dapat dibaca")
        return None

def hitung_ipk(nilai_matkul):
    konversi_grade = {
        "A" : 4,
        "B" : 3,
        "C" : 2,
        "D" : 1,
        "E" : 0
    }
    jum_sks = 0
    jum_nilai = 0
    for matkul in nilai_matkul:
        sks = matkul["sks"]
        jum_sks += sks
        if matkul["nilai"] in konversi_grade:
            jum_nilai += sks * konversi_grade[matkul["nilai"]]
    return jum_nilai / jum_sks

data_nilai = load_data()
if data_nilai:
    ipk = hitung_ipk(data_nilai)
    print(ipk)