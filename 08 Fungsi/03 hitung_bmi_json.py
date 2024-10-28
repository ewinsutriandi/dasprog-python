import json
def load_data():
    try:
        with open('data/mock_bmi_siswa.json') as f:
            d = json.load(f)
            return d
    except FileNotFoundError:
        print("File tidak ditemukan")

def hitung_bmi(bb,tb):
    ''' Fungsi klasifikasi BMI, menghasilkan nilai bmi
    arguments:  
    * bb : berat badan dalam satuan kg.  
    * tb : tinggi badan dalam satuan cm.  

    returns -> nilai bmi
    '''
    tb_m = tb / 100 # konversi satuan tinggi ke meter
    bmi = bb / tb_m ** 2
    return bmi

def kelompok_bmi(bmi):
    ''' Fungsi klasifikasi BMI, menghasilkan jenis badan nilai bmi  
    arguments:  
    * bmi : indeks masa tubuh  
    returns -> kurus, langsing, gemuk, obesitas
    '''    

    if bmi >= 30:
        return "obesitas"
    elif bmi >= 25:
        return "gemuk"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "kurus"
    

data_bmi = load_data()

for siswa in data_bmi:
    bb = siswa['berat_badan']
    tb = siswa['tinggi_badan']
    bmi = hitung_bmi(bb,tb)
    kategori = kelompok_bmi(bmi)
    print(f"{siswa['nama']} BB: {bb} kg, TB: {tb} cm, BMI: {bmi:.2f}, Kategori: {kategori}")