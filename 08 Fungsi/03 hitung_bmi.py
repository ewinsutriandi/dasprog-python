def kelompok_bmi(bb,tb):
    ''' Fungsi klasifikasi BMI, menghasilkan jenis badan berdasarkan tinggi dan berat badan  
    arguments:  
    * bb : berat badan dalam satuan kg.  
    * tb : tinggi badan dalam satuan cm.  

    returns -> kurus, langsing, gemuk, obesitas
    '''
    tb_m = tb / 100 # konversi satuan tinggi ke meter
    bmi = bb / tb_m ** 2

    if bmi >= 30:
        return "obesitas"
    elif bmi >= 25:
        return "gemuk"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "kurus"

# contoh pemakaian
bb_upin = 60
tb_upin = 155
print(f"Upin dengan tinggi {tb_upin} dan berat {bb_upin} tergolong {kelompok_bmi(bb_upin,tb_upin)}")
